#!/usr/bin/env python3

import argparse
import json
import subprocess
from pathlib import Path

import requests

DEMO_HOST = 'https://demo.defectdojo.org'
OAS_URL = 'https://github.com/DefectDojo/django-DefectDojo/releases/download/%s/oas.json'
LATEST_OAS_URL = 'https://github.com/DefectDojo/django-DefectDojo/releases/latest/download/oas.json'
FILE = Path(__file__).parent / 'openapi.json'
SCRIPTS = Path(__file__).parent.parent / 'integration'


def fetch_instance(host):
    r = requests.get(f'{host}/api/v2/oa3/schema/', params={'format': 'json'})
    r.raise_for_status()
    with FILE.open('w') as f:
        json.dump(r.json(), f, indent=4)


def fetch_github(version: str | None):
    url = OAS_URL % version if version else LATEST_OAS_URL
    r = requests.get(url)
    r.raise_for_status()
    with FILE.open('w') as f:
        json.dump(r.json(), f, indent=4)


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
    args = p.parse_args()

    if args.demo:
        host = DEMO_HOST
    elif args.compose:
        subprocess.check_call([SCRIPTS / 'run_dojo.sh'])
        host = 'http://localhost:8080'
    else:
        return fetch_github(args.version)

    if args.version:
        raise argparse.ArgumentError('--version can only be used with github releases')

    try:
        fetch_instance(host)
    finally:
        if not args.demo:
            subprocess.check_call([SCRIPTS / 'stop_dojo.sh'])


if __name__ == '__main__':
    main()
