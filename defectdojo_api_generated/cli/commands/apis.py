"""Dynamic API command registration for the CLI."""

import importlib
import inspect
import pkgutil

import classyclick

from defectdojo_api_generated import api as api_package
from defectdojo_api_generated.client import DefectDojo

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


def _build_api_group(module_name: str, api_class: type) -> type:
    group_name = module_name.removesuffix('_api').replace('_', '-')

    class ApiGroup(CLI.SubGroup, classyclick.Group):
        __config__ = classyclick.Group.Config(
            name=group_name,
            help=f'`{api_class.__name__}`.',
        )
        client: DefectDojo = classyclick.ContextMeta('client')

    methods = sorted(name for name, member in inspect.getmembers(api_class, callable) if not name.startswith('_'))
    method_set = set(methods)
    for method in methods:
        if method.endswith('_with_http_info') or method.endswith('_without_preload_content'):
            continue
        if method.endswith('list') and f'{method}_iterator' in method_set:
            continue
        method_name = method
        if method.endswith('_iterator') and method[:-9] in method_set:
            method_name = method[:-9]

        class ApiCommand(ApiGroup.Command, classyclick.Command):
            __config__ = classyclick.Command.Config(
                name=method_name,
                help=f'`{method}`.',
            )

            def __call__(self):
                pass

    return ApiGroup


for _module_name, _api_class in _iter_api_modules():
    _command = _build_api_group(_module_name, _api_class)
    API_COMMANDS[_module_name] = _command
