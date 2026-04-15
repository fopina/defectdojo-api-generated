#!/usr/bin/env -S python3 -u

import argparse
import re
from pathlib import Path

VERSION_PY = Path(__file__).parent.parent / 'defectdojo_api_generated' / '__init__.py'
VERSION_RE = re.compile(r"__version__ = '(.*?)'")
CLI_DEPENDENCY_PYPROJECT = Path(__file__).parent.parent / 'packages' / 'cli' / 'pyproject.toml'
CLI_VERSION_RE = re.compile(r'(^version = ")([^"]+)(")', re.MULTILINE)
CLI_DEPENDENCY_RE = re.compile(r'("defectdojo-api-generated==)([^"]+)(")')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--set', type=str, metavar='VERSION', help='New version')
    args = p.parse_args()

    data = VERSION_PY.read_text()
    version = VERSION_RE.findall(data)
    if not version:
        raise Exception('could not find version')
    version = version[0]
    print(f'Current version: {version}')

    if args.set:
        VERSION_PY.write_text(VERSION_RE.sub(f"__version__ = '{args.set}'", data))
        cli_pyproject_data = CLI_DEPENDENCY_PYPROJECT.read_text()
        cli_pyproject_data = CLI_VERSION_RE.sub(rf'\g<1>{args.set}\g<3>', cli_pyproject_data)
        CLI_DEPENDENCY_PYPROJECT.write_text(CLI_DEPENDENCY_RE.sub(rf'\g<1>{args.set}\g<3>', cli_pyproject_data))
        print(f'New version: {args.set}')


if __name__ == '__main__':
    main()
