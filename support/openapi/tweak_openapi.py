#!/usr/bin/env python3

import json
from pathlib import Path

FILE = Path(__file__).parent / 'openapi.json'
BUILD = Path(__file__).parent / 'build' / 'openapi.json'


def tweak_paginated(data):
    for path, path_value in data['paths'].items():
        try:
            schema_ref = path_value['get']['responses']['200']['content']['application/json']['schema']['$ref']
        except KeyError:
            continue

        if not schema_ref.startswith('#/components/schemas/Paginated'):
            continue

        return_type = schema_ref.rsplit('/', 1)[-1]
        return_obj = data['components']['schemas'][return_type]
        item_return_type = return_obj['properties']['results']['items']['$ref'].rsplit('/', 1)[-1]
        path_value['get'].update(
            {
                'x-has-iterator': True,
                'x-iterator-item': item_return_type,
            }
        )


def main():
    BUILD.parent.mkdir(exist_ok=True)
    with FILE.open('r') as inp:
        data = json.load(inp)

    tweak_paginated(data)

    with BUILD.open('w') as out:
        json.dump(data, out, indent=4)


if __name__ == '__main__':
    main()
