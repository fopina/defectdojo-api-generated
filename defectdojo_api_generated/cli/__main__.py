"""Command-line entrypoint for defectdojo_api_generated."""

import importlib
import pkgutil
import sys
from pathlib import Path


def discover_commands():
    for _, module_name, _ in pkgutil.iter_modules([Path(__file__).parent / 'commands']):
        importlib.import_module(f'{__package__}.commands.{module_name}')


def load_cli():
    try:
        from .commands.cli import CLI
    except ModuleNotFoundError as exc:
        print(
            'The DefectDojo CLI requires extra dependencies. '
            'Install them using "defectdojo-api-generated[cli]" as package',
            file=sys.stderr,
        )
        raise SystemExit(1) from exc

    return CLI


def main():
    CLI = load_cli()
    discover_commands()
    CLI.click()


if __name__ == '__main__':
    main()
