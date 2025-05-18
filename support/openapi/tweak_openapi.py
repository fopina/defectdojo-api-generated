#!/usr/bin/env python3

import json
from pathlib import Path

FILE = Path(__file__).parent / 'openapi.json'
BUILD = Path(__file__).parent / 'build' / 'openapi.json'


def main():
    BUILD.parent.mkdir(exist_ok=True)
    with FILE.open('r') as inp:
        data = json.load(inp)

    # nothing done for now...

    with BUILD.open('w') as out:
        json.dump(data, out, indent=4)


if __name__ == '__main__':
    main()
