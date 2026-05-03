"""Dynamic API command registration for the CLI."""

import datetime
import decimal
import importlib
import inspect
import json
import pkgutil
import types
from pathlib import Path
from typing import Annotated, Any, Optional, Union, get_args, get_origin

import classyclick
import click
from pydantic import BaseModel

from defectdojo_api_generated import api as api_package
from defectdojo_api_generated.client import DefectDojo
from defectdojo_api_generated.exceptions import BadRequestException
from defectdojo_api_generated.helpers import IteratorResult

from .cli import CLI

_PRIMITIVE_CLICK_TYPES = (
    bool,
    bytes,
    str,
    int,
    float,
    datetime.date,
    datetime.datetime,
    decimal.Decimal,
)


class API(CLI.SubGroup, classyclick.Group):
    """Interact directly with any API/method"""


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


def _get_help_from_annotation(annotation: Any) -> Optional[str]:
    if get_origin(annotation) is Annotated:
        _, *metadata = get_args(annotation)
        for item in metadata:
            description = getattr(item, 'description', None)
            if description:
                return description

    return None


def _is_primitive_click_type(annotation: Any) -> bool:
    return inspect.isclass(annotation) and annotation in _PRIMITIVE_CLICK_TYPES


def _is_model_click_type(annotation: Any) -> bool:
    return inspect.isclass(annotation) and issubclass(annotation, BaseModel)


def _is_file_upload_union(annotation: Any) -> bool:
    origin = get_origin(annotation)
    if origin is Annotated:
        return _is_file_upload_union(get_args(annotation)[0])

    if origin is Union or origin is getattr(types, 'UnionType', None):
        args = [arg for arg in get_args(annotation) if arg is not type(None)]
        normalized = set()
        for arg in args:
            arg_origin = get_origin(arg)
            if arg_origin is Annotated:
                arg = get_args(arg)[0]
                arg_origin = get_origin(arg)

            if arg is bytes:
                normalized.add('bytes')
            elif arg is str:
                normalized.add('str')
            elif arg_origin is tuple:
                tuple_args = []
                for item in get_args(arg):
                    item_origin = get_origin(item)
                    if item_origin is Annotated:
                        item = get_args(item)[0]
                    tuple_args.append(item)
                if tuple_args == [str, bytes]:
                    normalized.add('tuple[str,bytes]')

        return normalized == {'bytes', 'str', 'tuple[str,bytes]'}

    return False


def _coerce_file_upload_value(value: Any):
    if value is None:
        return None

    path = Path(value)
    return (path.name, path.read_bytes())


def _convert_cli_value(name: str, value: Any, converter: Optional[type[BaseModel]], *, multiple: bool):
    if name == 'file':
        if multiple:
            return tuple(_coerce_file_upload_value(item) for item in value)
        return _coerce_file_upload_value(value)

    if converter is None:
        return value

    if multiple:
        return tuple(converter.model_validate_json(item) for item in value)

    if value is None:
        return None

    return converter.model_validate_json(value)


def _get_click_type(
    annotation: Any, *, parameter_name: Optional[str] = None
) -> tuple[Any, bool, Optional[type[BaseModel]]]:
    multiple = False
    current = annotation

    while True:
        if current is inspect.Signature.empty:
            return Any, multiple, None

        origin = get_origin(current)
        if origin is Annotated:
            current = get_args(current)[0]
            continue

        if origin is None:
            if current is Any or _is_primitive_click_type(current):
                return current, multiple, None
            if _is_model_click_type(current):
                return str, multiple, current

            param_name = f' for parameter "{parameter_name}"' if parameter_name else ''
            raise TypeError(
                f'Unsupported CLI parameter type{param_name}: {current!r}. Only primitive types are supported.'
            )

        if origin is list:
            multiple = True
            list_args = get_args(current)
            current = list_args[0] if list_args else Any
            continue

        if origin is tuple:
            tuple_args = get_args(current)
            current = tuple_args[0] if tuple_args else Any
            continue

        if origin is Union or origin is getattr(types, 'UnionType', None):
            if _is_file_upload_union(current):
                return Path, multiple, None

            union_args = [arg for arg in get_args(current) if arg is not type(None)]
            if not union_args:
                return Any, multiple, None
            current = union_args[0]
            continue

        if current is Any or _is_primitive_click_type(current):
            return current, multiple, None
        if _is_model_click_type(current):
            return str, multiple, current

        param_name = f' for parameter "{parameter_name}"' if parameter_name else ''
        raise TypeError(f'Unsupported CLI parameter type{param_name}: {current!r}. Only primitive types are supported.')


def _get_class_annotation(click_type: Any) -> type:
    if click_type is Any:
        return str
    return click_type


def _build_option(
    click_type: Any,
    *,
    help_text: Optional[str],
    required: bool = False,
    default: Any = None,
    multiple: bool = False,
    short_name: Optional[str] = None,
):
    option_kwargs = {'help': help_text}
    if required:
        option_kwargs['required'] = True
    else:
        option_kwargs['default'] = default
    if click_type is not Any:
        option_kwargs['type'] = click_type
    if multiple:
        option_kwargs['multiple'] = True

    if short_name is not None:
        return classyclick.Option(f'-{short_name}', default_parameter=False, **option_kwargs)
    return classyclick.Option(**option_kwargs)


def _add_shared_output_options(namespace: dict[str, Any]) -> None:
    namespace['json'] = classyclick.Option(help='Dump responses as JSON')
    namespace['jq'] = classyclick.Option(help='Apply a JMESPath expression to each response item', default=None)
    namespace['__annotations__']['json'] = bool
    namespace['__annotations__']['jq'] = str


def _add_parameter_options(
    namespace: dict[str, Any],
    parameters: list[tuple[str, Any, Any, bool, Optional[type[BaseModel]]]],
    *,
    help_getter,
    default_getter,
) -> None:
    required_parameters = [item for item in parameters if default_getter(item) is inspect.Signature.empty]
    optional_parameters = [item for item in parameters if default_getter(item) is not inspect.Signature.empty]

    for name, source, click_type, multiple, _converter in required_parameters:
        namespace['__annotations__'][name] = _get_class_annotation(click_type)
        namespace[name] = _build_option(
            click_type,
            help_text=help_getter(source),
            required=True,
            multiple=multiple,
            short_name=name if len(name) == 1 else None,
        )

    _add_shared_output_options(namespace)

    for name, source, click_type, multiple, _converter in optional_parameters:
        namespace['__annotations__'][name] = _get_class_annotation(click_type)
        namespace[name] = _build_option(
            click_type,
            help_text=help_getter(source),
            default=default_getter((name, source, click_type, multiple, _converter)),
            multiple=multiple,
            short_name=name if len(name) == 1 else None,
        )


def _iter_command_parameters(api_class: type, target_method: str):
    signature = inspect.signature(getattr(api_class, target_method))

    for name, parameter in signature.parameters.items():
        if name == 'self' or name.startswith('_'):
            continue
        if parameter.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            continue

        yield name, parameter


def _get_request_model_type(annotation: Any) -> Optional[type[BaseModel]]:
    _, _, converter = _get_click_type(annotation)
    if converter is not None and converter.__name__.endswith('Request'):
        return converter
    return None


def _get_model_field_help(field: Any) -> Optional[str]:
    return field.description or _get_help_from_annotation(field.annotation)


def _build_command_namespace(command_name: str, api_class: type, target_method: str) -> dict[str, Any]:
    return {
        '__config__': classyclick.Command.Config(
            name=command_name,
            help=_get_command_help(api_class, target_method),
        ),
        'client': classyclick.ContextMeta('client'),
        '__annotations__': {
            'client': DefectDojo,
        },
    }


def _build_command_class(parent_class: type, namespace: dict[str, Any]) -> type:
    return type(
        'ApiCommand',
        (parent_class, classyclick.Command),
        namespace,
    )


def _collect_command_values(parameters, getter, *, should_include):
    values = {}
    for name, source, _, multiple, converter in parameters:
        value = getter(name)
        value = _convert_cli_value(name, value, converter, multiple=multiple)
        if should_include(value=value, source=source, multiple=multiple):
            values[name] = value
    return values


def _render_api_result(result: Any, instance: Any) -> None:
    _render_result(
        result,
        json_mode=instance.json,
        jq_expression=instance.jq,
        max_records=getattr(instance, 'max_records', None),
    )


def _create_standard_command_call(api_class: type, target_method: str, command_parameters):
    def __call__(self):
        method = getattr(api_class(self.client.api_client), target_method)
        kwargs = _collect_command_values(
            command_parameters,
            lambda name: getattr(self, name),
            should_include=lambda *, value, source, multiple: value if multiple else value != source.default,
        )
        result = _invoke_api_method(method, **kwargs)
        _render_api_result(result, self)

    return __call__


def _create_model_command_call(api_class: type, target_method: str, field_definitions, model_class: type[BaseModel]):
    def __call__(self):
        method = getattr(api_class(self.client.api_client), target_method)
        request_data = _collect_command_values(
            field_definitions,
            lambda name: getattr(self, name),
            should_include=lambda *, value, source, multiple: value
            if multiple
            else value != source.default and value is not None,
        )
        request_model = model_class.model_validate(request_data)
        result = _invoke_api_method(method, request_model)
        _render_api_result(result, self)

    return __call__


def _build_model_field_definitions(model_class: type[BaseModel]):
    field_definitions = []

    for field_name, field in model_class.model_fields.items():
        click_type, multiple, converter = _get_click_type(field.annotation, parameter_name=field_name)
        field_definitions.append((field_name, field, click_type, multiple, converter))

    field_definitions.sort(key=lambda item: not item[1].is_required())
    return field_definitions


def _build_model_field_command(
    api_class: type,
    command_name: str,
    target_method: str,
    *,
    parent_class: type,
    model_class: type[BaseModel],
) -> type:
    field_definitions = _build_model_field_definitions(model_class)
    namespace = _build_command_namespace(command_name, api_class, target_method)
    namespace['__call__'] = _create_model_command_call(api_class, target_method, field_definitions, model_class)

    _add_parameter_options(
        namespace,
        field_definitions,
        help_getter=_get_model_field_help,
        default_getter=lambda item: item[1].default if not item[1].is_required() else inspect.Signature.empty,
    )

    return _build_command_class(parent_class, namespace)


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


def _apply_jq(value: Any, jq_expression: Optional[str]) -> Any:
    if not jq_expression:
        return value

    try:
        import jmespath
    except ModuleNotFoundError as exc:
        raise click.ClickException('jq support requires the jmespath package') from exc

    return jmespath.search(jq_expression, _to_jsonable(value))


def _get_bad_request_detail(exc: BadRequestException) -> str:
    for candidate in (exc.data, exc.body, exc.reason):
        if candidate is None:
            continue

        if isinstance(candidate, BaseModel):
            candidate = candidate.model_dump(mode='json', exclude_none=True)

        if isinstance(candidate, str):
            try:
                candidate = json.loads(candidate)
            except json.JSONDecodeError:
                if candidate.strip():
                    return candidate
                continue

        if isinstance(candidate, dict):
            for key in ('detail', 'message', 'error'):
                value = candidate.get(key)
                if value:
                    return str(value)
            continue

        text = str(candidate).strip()
        if text:
            return text

    return str(exc)


def _invoke_api_method(method, *args, **kwargs):
    try:
        return method(*args, **kwargs)
    except BadRequestException as exc:
        raise click.ClickException(_get_bad_request_detail(exc)) from exc


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


def _render_result(result: Any, *, json_mode: bool, jq_expression: Optional[str], max_records: Optional[int] = None):
    div = False
    emitted = 0
    for item in _iter_output_items(result):
        if max_records is not None and emitted >= max_records:
            break

        item = _apply_jq(item, jq_expression)

        if json_mode:
            click.echo(json.dumps(_to_jsonable(item), ensure_ascii=False, default=str))
        else:
            if div:
                click.echo('\n---\n')
            else:
                div = True
            click.echo(_format_text_item(item))

        emitted += 1


def make_api_command(api_class: type, command_name: str, target_method: str, *, parent_class: type):
    raw_parameters = list(_iter_command_parameters(api_class, target_method))
    if len(raw_parameters) == 1:
        _, parameter = raw_parameters[0]
        request_model_type = _get_request_model_type(parameter.annotation)
        if request_model_type is not None:
            return _build_model_field_command(
                api_class,
                command_name,
                target_method,
                parent_class=parent_class,
                model_class=request_model_type,
            )

    command_parameters = sorted(
        [
            (name, parameter, *_get_click_type(parameter.annotation, parameter_name=name))
            for name, parameter in raw_parameters
        ],
        key=lambda item: item[1].default is not inspect.Signature.empty,
    )
    namespace = _build_command_namespace(command_name, api_class, target_method)
    namespace['__call__'] = _create_standard_command_call(api_class, target_method, command_parameters)

    _add_parameter_options(
        namespace,
        command_parameters,
        help_getter=lambda parameter: _get_help_from_annotation(parameter.annotation),
        default_getter=lambda item: item[1].default,
    )

    if target_method.endswith('_iterator'):
        namespace['__annotations__']['max_records'] = Optional[int]
        namespace['max_records'] = classyclick.Option(
            '-m',
            type=click.IntRange(min=1),
            default=None,
            help='Maximum number of records to emit.',
        )

    return _build_command_class(parent_class, namespace)


def make_api_group(module_name: str, api_class: type) -> type:
    group_name = module_name.removesuffix('_api').replace('_', '-')
    command_methods = list(_iter_command_methods(api_class))

    if len(command_methods) == 1:
        _, target_method = command_methods[0]
        return make_api_command(api_class, group_name, target_method, parent_class=API.Command)

    class ApiGroup(API.SubGroup, classyclick.Group):
        __config__ = classyclick.Group.Config(
            name=group_name,
            help=f'methods from `{api_class.__name__}`.',
        )

    for command_name, target_method in command_methods:
        make_api_command(api_class, command_name, target_method, parent_class=ApiGroup.Command)

    return ApiGroup


for _module_name, _api_class in _iter_api_modules():
    make_api_group(_module_name, _api_class)
