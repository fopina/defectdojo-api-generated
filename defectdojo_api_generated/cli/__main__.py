"""Command-line entrypoint for defectdojo_api_generated."""

import importlib
import pkgutil
from pathlib import Path

from .commands.cli import CLI


def discover_commands():
    for loader, module_name, is_pkg in pkgutil.iter_modules([Path(__file__).parent / 'commands']):
        print(module_name)
        importlib.import_module(f'{__package__}.commands.{module_name}')


def main():
    discover_commands()
    CLI.click()


if __name__ == '__main__':
    main()
