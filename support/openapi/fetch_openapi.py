#!/usr/bin/env python3

import argparse
import json
import subprocess
from pathlib import Path
from typing import Optional

import requests

DEMO_HOST = 'https://demo.defectdojo.org'
OAS_URL = 'https://github.com/DefectDojo/django-DefectDojo/releases/download/%s/oas.json'
LATEST_OAS_URL = 'https://github.com/DefectDojo/django-DefectDojo/releases/latest/download/oas.json'
FILE = Path(__file__).parent / 'openapi.json'
SCRIPTS = Path(__file__).parent.parent / 'integration'


def write_schema(data: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w') as f:
        json.dump(data, f, indent=4)


def fetch_instance(host, output: Path):
    r = requests.get(f'{host}/api/v2/oa3/schema/', params={'format': 'json'})
    r.raise_for_status()
    write_schema(r.json(), output)


def fetch_github(version: Optional[str], output: Path):
    url = OAS_URL % version if version else LATEST_OAS_URL
    r = requests.get(url)
    r.raise_for_status()
    write_schema(r.json(), output)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--demo', action='store_true', help='Use live demo instead of github releases')
    p.add_argument(
        '-c',
        '--compose',
        action='store_true',
        help='Use local compose (from integration tests) instead of github releases',
    )
    p.add_argument(
        '-v',
        '--version',
        type=str,
        help='Fetch this specific version instead of latest (it can only used for github releases)',
    )
    p.add_argument(
        '-o',
        '--output',
        type=Path,
        default=FILE,
        help=f'Write the fetched schema to this file (default: {FILE})',
    )
    args = p.parse_args()

    if args.demo:
        host = DEMO_HOST
    elif args.compose:
        subprocess.check_call([SCRIPTS / 'run_dojo.sh'])
        host = 'http://localhost:8080'
    else:
        return fetch_github(args.version, args.output)

    if args.version:
        raise argparse.ArgumentError('--version can only be used with github releases')

    try:
        fetch_instance(host, args.output)
    finally:
        if not args.demo:
            subprocess.check_call([SCRIPTS / 'stop_dojo.sh'])


if __name__ == '__main__':
    main()
