"""Command-line entrypoint for defectdojo_api_generated."""

from __future__ import annotations

import argparse
import json
import os
from typing import Any, Optional, Sequence

from defectdojo_api_generated import __version__
from defectdojo_api_generated.client import DefectDojo


def _get_env(name: str) -> Optional[str]:
    value = os.environ.get(name)
    return value if value else None


def _serialize_payload(payload: Any) -> str:
    if hasattr(payload, 'model_dump'):
        payload = payload.model_dump(by_alias=True, exclude_none=True)

    return json.dumps(payload, indent=2, sort_keys=True)


def _print_payload(payload: Any) -> None:
    serialized = _serialize_payload(payload)

    try:
        from rich.console import Console

        Console().print_json(serialized)
    except ImportError:
        print(serialized)


def _build_client(args: argparse.Namespace, parser: argparse.ArgumentParser) -> DefectDojo:
    token = args.token
    username = args.username
    password = args.password

    if not args.base_url:
        parser.error('`--base-url` or `DEFECTDOJO_BASE_URL` is required for API commands.')
    if token and (username or password):
        parser.error('Provide `--token` or `--username`/`--password`, not both.')
    if bool(username) != bool(password):
        parser.error('Provide both `--username` and `--password` for basic auth.')
    if token is None and username is None:
        parser.error('Authentication is required: use `--token` or `--username`/`--password`.')

    auth = (username, password) if username and password else None
    return DefectDojo(
        base_url=args.base_url,
        token=token,
        auth=auth,
        verify_ssl=not args.insecure,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='defectdojo', description='CLI for the DefectDojo generated API client.')
    parser.add_argument('--base-url', default=_get_env('DEFECTDOJO_BASE_URL'), help='DefectDojo base URL.')
    parser.add_argument('--token', default=_get_env('DEFECTDOJO_TOKEN'), help='DefectDojo API token.')
    parser.add_argument('--username', default=_get_env('DEFECTDOJO_USERNAME'), help='Basic auth username.')
    parser.add_argument('--password', default=_get_env('DEFECTDOJO_PASSWORD'), help='Basic auth password.')
    parser.add_argument('--insecure', action='store_true', help='Disable TLS certificate verification.')

    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('version', help='Print the installed package version.')
    subparsers.add_parser('user-profile', help='Fetch the authenticated user profile.')
    subparsers.add_parser('system-settings', help='Fetch DefectDojo system settings.')
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == 'version':
        print(__version__)
        return 0

    client = _build_client(args, parser)

    if args.command == 'user-profile':
        payload = client.user_profile_api.retrieve()
        _print_payload(payload)
        return 0

    if args.command == 'system-settings':
        payload = client.system_settings_api.list()
        _print_payload(payload)
        return 0

    parser.error(f'Unknown command: {args.command}')
    return 2
