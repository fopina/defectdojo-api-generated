#!/usr/bin/env python3

import argparse
import json
import subprocess
from pathlib import Path

import requests

DEMO_HOST = 'https://demo.defectdojo.org'
FILE = Path(__file__).parent / 'openapi.json'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-d', '--demo', action='store_true', help='Use live demo instead of local Dojo instance')
    args = p.parse_args()
    if args.demo:
        host = DEMO_HOST
    else:
        subprocess.check_call([Path(__file__).parent / 'integration' / 'run_dojo.sh'])
        host = 'http://localhost:8080'

    try:
        r = requests.get(f'{host}/api/v2/oa3/schema/', params={'format': 'json'})
        r.raise_for_status()
        with FILE.open('w') as f:
            json.dump(r.json(), f, indent=4)
    finally:
        if not args.demo:
            subprocess.check_call([Path(__file__).parent / 'integration' / 'stop_dojo.sh'])


if __name__ == '__main__':
    main()
