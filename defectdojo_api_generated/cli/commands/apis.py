"""Dynamic API command registration for the CLI."""

import importlib
import inspect
import json
import pkgutil
from typing import Annotated, Any, Union, get_args, get_origin

import classyclick
import click
from pydantic import BaseModel

from defectdojo_api_generated import api as api_package
from defectdojo_api_generated.client import DefectDojo
from defectdojo_api_generated.helpers import IteratorResult

from .cli import CLI

API_COMMANDS = {}


def _iter_api_modules():
    for _, module_name, _ in pkgutil.iter_modules(api_package.__path__):
        if module_name == '__init__':
            continue

        module = importlib.import_module(f'{api_package.__name__}.{module_name}')
        api_classes = [
            value
            for _, value in inspect.getmembers(module, inspect.isclass)
            if value.__module__ == module.__name__ and value.__name__.endswith('Api')
        ]
        if len(api_classes) != 1:
            continue

        yield module_name, api_classes[0]


def _iter_command_methods(api_class: type):
    methods = sorted(name for name, member in inspect.getmembers(api_class, callable) if not name.startswith('_'))
    method_set = set(methods)

    for method in methods:
        if method.endswith('_with_http_info') or method.endswith('_without_preload_content'):
            continue
        if method.endswith('list') and f'{method}_iterator' in method_set:
            continue
        command_name = method
        if method.endswith('_iterator') and method[:-9] in method_set:
            command_name = method[:-9]
        yield command_name.replace('_', '-'), method


def _get_command_help(api_class: type, target_method: str) -> str:
    doc_targets = [target_method]
    if target_method.endswith('_iterator'):
        doc_targets.append(target_method[:-9])

    for method_name in doc_targets:
        method = getattr(api_class, method_name, None)
        doc = inspect.getdoc(method)
        if doc:
            return doc.splitlines()[0].strip()

    return f'`{target_method}`.'


def _get_help_from_annotation(annotation: Any) -> str | None:
    if get_origin(annotation) is Annotated:
        _, *metadata = get_args(annotation)
        for item in metadata:
            description = getattr(item, 'description', None)
            if description:
                return description

    return None


def _get_click_type(annotation: Any) -> tuple[Any, bool]:
    multiple = False
    current = annotation

    while True:
        if current is inspect.Signature.empty:
            return Any, multiple

        origin = get_origin(current)
        if origin is Annotated:
            current = get_args(current)[0]
            continue

        if origin is None:
            return current, multiple

        if origin is list:
            multiple = True
            list_args = get_args(current)
            current = list_args[0] if list_args else Any
            continue

        if origin is tuple:
            tuple_args = get_args(current)
            current = tuple_args[0] if tuple_args else Any
            continue

        if origin is Union:
            union_args = [arg for arg in get_args(current) if arg is not type(None)]
            if not union_args:
                return Any, multiple
            current = union_args[0]
            continue

        return current, multiple


def _iter_command_parameters(api_class: type, target_method: str):
    signature = inspect.signature(getattr(api_class, target_method))

    for name, parameter in signature.parameters.items():
        if name == 'self' or name.startswith('_'):
            continue
        if parameter.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            continue
        if parameter.default is inspect.Signature.empty:
            continue

        yield name, parameter


def _iter_output_items(result):
    if isinstance(result, IteratorResult):
        yield from _iter_output_items(result.result)
        return

    if isinstance(result, (list, tuple)):
        for item in result:
            yield from _iter_output_items(item)
        return

    if inspect.isgenerator(result):
        for item in result:
            yield from _iter_output_items(item)
        return

    yield result


def _to_jsonable(value: Any, *, exclude_none: bool = False) -> Any:
    if isinstance(value, BaseModel):
        return value.model_dump(mode='json', exclude_none=exclude_none)

    if isinstance(value, dict):
        return {
            key: _to_jsonable(item, exclude_none=exclude_none)
            for key, item in value.items()
            if not (exclude_none and item is None)
        }

    if isinstance(value, (list, tuple)):
        return [_to_jsonable(item, exclude_none=exclude_none) for item in value if not (exclude_none and item is None)]

    return value


def _apply_jq(value: Any, jq_expression: str | None) -> Any:
    if not jq_expression:
        return value

    try:
        import jmespath
    except ModuleNotFoundError as exc:
        raise click.ClickException('jq support requires the jmespath package') from exc

    return jmespath.search(jq_expression, _to_jsonable(value))


def _format_text_value(value: Any) -> str:
    if isinstance(value, (dict, list, tuple, BaseModel)):
        return json.dumps(_to_jsonable(value, exclude_none=True), ensure_ascii=False, default=str)
    return str(value)


def _format_text_item(item: Any) -> str:
    if isinstance(item, BaseModel):
        payload = item.model_dump(mode='json', exclude_none=True)
    elif isinstance(item, dict):
        payload = {key: value for key, value in item.items() if value is not None}
    elif isinstance(item, (list, tuple)):
        return json.dumps(_to_jsonable(item, exclude_none=True), ensure_ascii=False, default=str)
    else:
        return str(item)

    lines = []
    for key, value in payload.items():
        lines.append(f'{click.style(str(key), bold=True)}: {_format_text_value(value)}')
    return '\n'.join(lines)


def _render_result(result: Any, *, json_mode: bool, jq_expression: str | None):
    div = False
    for item in _iter_output_items(result):
        item = _apply_jq(item, jq_expression)

        if json_mode:
            click.echo(json.dumps(_to_jsonable(item), ensure_ascii=False, default=str))
        else:
            if div:
                click.echo('\n---\n')
            else:
                div = True
            click.echo(_format_text_item(item))


def make_api_command(api_class: type, command_name: str, target_method: str, *, parent_class: type):
    command_parameters = [
        (name, parameter, *_get_click_type(parameter.annotation))
        for name, parameter in _iter_command_parameters(api_class, target_method)
    ]

    def __call__(self):
        method = getattr(api_class(self.client.api_client), target_method)
        kwargs = {}
        for name, parameter, _, multiple in command_parameters:
            value = getattr(self, name)
            if multiple:
                if value:
                    kwargs[name] = value
            elif value != parameter.default:
                kwargs[name] = value
        _render_result(method(**kwargs), json_mode=self.json, jq_expression=self.jq)

    namespace = {
        '__config__': classyclick.Command.Config(
            name=command_name,
            help=_get_command_help(api_class, target_method),
        ),
        '__call__': __call__,
        'client': classyclick.ContextMeta('client'),
        'json': classyclick.Option(help='Dump responses as JSON'),
        'jq': classyclick.Option(help='Apply a JMESPath expression to each response item', default=None),
        '__annotations__': {
            'client': DefectDojo,
            'json': bool,
            'jq': str,
        },
    }

    for name, parameter, click_type, multiple in command_parameters:
        namespace['__annotations__'][name] = click_type
        option_kwargs = {
            'help': _get_help_from_annotation(parameter.annotation),
            'default': parameter.default,
        }
        if click_type is not Any:
            option_kwargs['type'] = click_type
        if multiple:
            option_kwargs['multiple'] = True
        if len(name) == 1:
            namespace[name] = classyclick.Option(f'-{name}', default_parameter=False, **option_kwargs)
        else:
            namespace[name] = classyclick.Option(**option_kwargs)

    return type(
        'ApiCommand',
        (parent_class, classyclick.Command),
        namespace,
    )


def make_api_group(module_name: str, api_class: type) -> type:
    group_name = module_name.removesuffix('_api').replace('_', '-')
    command_methods = list(_iter_command_methods(api_class))

    if len(command_methods) == 1:
        _, target_method = command_methods[0]
        return make_api_command(api_class, group_name, target_method, parent_class=CLI.Command)

    class ApiGroup(CLI.SubGroup, classyclick.Group):
        __config__ = classyclick.Group.Config(
            name=group_name,
            help=f'methods from `{api_class.__name__}`.',
        )

    for command_name, target_method in command_methods:
        make_api_command(api_class, command_name, target_method, parent_class=ApiGroup.Command)

    return ApiGroup


for _module_name, _api_class in _iter_api_modules():
    _command = make_api_group(_module_name, _api_class)
    API_COMMANDS[_module_name] = _command
