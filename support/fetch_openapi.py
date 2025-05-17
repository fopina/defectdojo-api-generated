#!/usr/bin/env python3

import json
from pathlib import Path

import requests

HOST = 'https://demo.defectdojo.org'
FILE = Path(__file__).parent / 'openapi.json'


def main():
    r = requests.get(f'{HOST.rstrip("/")}/api/v2/oa3/schema/', params={'format': 'json'})
    r.raise_for_status()
    with FILE.open('w') as f:
        json.dump(r.json(), f, indent=4)


if __name__ == '__main__':
    main()
