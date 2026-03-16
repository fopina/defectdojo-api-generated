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


def tweak_required(data):
    for schema in data['components']['schemas'].values():
        try:
            del schema['required']
        except KeyError:
            """nothing to do"""


def tweak_operation_ids(data):
    """Encode full operationId prefixes so the generator strips them reliably.

    OpenAPI Generator's ``--remove-operation-id-prefix`` handling does not fully
    remove prefixes when they contain underscores (such `system_settings`).
    We infer the complete prefix from ``tags[0]`` for each operation,
    validate that it still matches the current ``operationId``,
    and replace underscores in just that prefix with ``S`` so the generator
    treats it as a single removable token.
    """
    for path, path_item in data['paths'].items():
        for method, operation in path_item.items():
            if not isinstance(operation, dict):
                continue

            operation_id = operation.get('operationId')
            if operation_id is None:
                continue

            try:
                tag = operation['tags'][0]
            except (KeyError, IndexError) as exc:
                raise ValueError(
                    f'Missing tags[0] for {method.upper()} {path} with operationId {operation_id!r}'
                ) from exc

            prefix = tag.replace('-', '_')
            if not operation_id.startswith(prefix):
                raise ValueError(
                    f'Expected tags[0]={tag!r} to be an operationId prefix for '
                    f'{method.upper()} {path}, got {operation_id!r}'
                )

            operation['operationId'] = operation_id.replace(prefix, prefix.replace('_', 'S'), 1)


def main():
    BUILD.parent.mkdir(exist_ok=True)
    with FILE.open('r') as inp:
        data = json.load(inp)

    tweak_operation_ids(data)
    tweak_paginated(data)
    tweak_required(data)

    with BUILD.open('w') as out:
        json.dump(data, out, indent=4)


if __name__ == '__main__':
    main()
