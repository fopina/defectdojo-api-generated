#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import Optional

CHANGELOG = Path(__file__).parent / 'OPENAPI_CHANGELOG.md'
HTTP_METHODS = {'get', 'post', 'put', 'patch', 'delete', 'options', 'head', 'trace'}


def load_json(path: Path) -> dict:
    with path.open() as handle:
        return json.load(handle)


def normalize_version(version: Optional[str]) -> str:
    if not version:
        return 'unknown'
    return version[1:] if version.startswith('v') else version


def get_version(data: dict) -> str:
    return normalize_version(data.get('info', {}).get('version'))


def collect_endpoints(data: dict) -> dict[str, dict]:
    endpoints = {}
    for path, path_item in data.get('paths', {}).items():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            endpoints[f'{method.upper()} {path}'] = operation
    return endpoints


def collect_models(data: dict) -> dict[str, dict]:
    return data.get('components', {}).get('schemas', {})


def build_diff(old_items: dict[str, dict], new_items: dict[str, dict]) -> tuple[list[str], list[str], list[str]]:
    old_keys = set(old_items)
    new_keys = set(new_items)

    added = sorted(new_keys - old_keys)
    removed = sorted(old_keys - new_keys)
    changed = sorted(key for key in old_keys & new_keys if old_items[key] != new_items[key])

    return added, removed, changed


def format_group(title: str, items: list[str]) -> list[str]:
    if not items:
        return []

    lines = [f'#### {title}']
    lines.extend(f'- `{item}`' for item in items)
    lines.append('')
    return lines


def format_section(title: str, endpoints: list[str], models: list[str]) -> list[str]:
    groups = [*format_group('Endpoints', endpoints), *format_group('Models', models)]
    if not groups:
        return []

    return [title, '', *groups]


def render_entry(old_data: dict, new_data: dict) -> str:
    new_endpoint_items, removed_endpoint_items, changed_endpoint_items = build_diff(
        collect_endpoints(old_data), collect_endpoints(new_data)
    )
    new_model_items, removed_model_items, changed_model_items = build_diff(
        collect_models(old_data), collect_models(new_data)
    )

    lines = [f'## v {get_version(new_data)} (from v {get_version(old_data)})', '']
    sections = [
        *format_section('### New', new_endpoint_items, new_model_items),
        *format_section('### Removed', removed_endpoint_items, removed_model_items),
        *format_section('### Changed', changed_endpoint_items, changed_model_items),
    ]

    if sections:
        lines.extend(sections)
    else:
        lines.extend(['No changes', ''])

    return '\n'.join(lines).strip() + '\n'


def update_changelog(old_path: Path, new_path: Path, changelog_path: Path = CHANGELOG) -> None:
    old_data = load_json(old_path)
    new_data = load_json(new_path)
    old_version = get_version(old_data)
    new_version = get_version(new_data)

    if old_version == new_version:
        print(f'Versions are the same ({new_version}); changelog not updated.')
        return

    entry = render_entry(old_data, new_data)

    previous = ''
    if changelog_path.exists():
        previous = changelog_path.read_text()
        if previous and not previous.startswith('\n'):
            previous = '\n' + previous

    changelog_path.write_text(entry + previous)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Compare two OpenAPI schema snapshots and prepend a summary to openapi_changelog.md.'
    )
    parser.add_argument('old_json', type=Path, help='Previous OpenAPI schema JSON file')
    parser.add_argument('new_json', type=Path, help='New OpenAPI schema JSON file')
    args = parser.parse_args()

    update_changelog(args.old_json, args.new_json)


if __name__ == '__main__':
    main()
