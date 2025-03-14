#!/usr/bin/env -S python3 -u

import argparse
import re
from pathlib import Path

# TODO: replace `example` with your package name
VERSION_PY = Path(__file__).parent.parent / 'example' / '__init__.py'
VERSION_RE = re.compile(r"__version__ = version = '(.*?)'")


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
        VERSION_PY.write_text(VERSION_RE.sub(f"__version__ = version = '{args.set}'", data))
        print(f'New version: {args.set}')


if __name__ == '__main__':
    main()
