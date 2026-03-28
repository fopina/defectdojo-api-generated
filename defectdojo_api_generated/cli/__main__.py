"""Command-line entrypoint for defectdojo_api_generated."""

import sys


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
    CLI.click()


if __name__ == '__main__':
    main()
