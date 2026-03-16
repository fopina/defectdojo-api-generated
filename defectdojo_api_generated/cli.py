"""Command-line entrypoint for defectdojo_api_generated."""

import json
import os
from dataclasses import dataclass
from typing import Any, Optional, Sequence

import click
from classyclick import Command, Context, ContextObj, Group, Option

from defectdojo_api_generated import __version__
from defectdojo_api_generated.client import DefectDojo


@dataclass
class CliConfig:
    base_url: Optional[str]
    token: Optional[str]
    username: Optional[str]
    password: Optional[str]
    insecure: bool


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


def _build_client(config: CliConfig) -> DefectDojo:
    if not config.base_url:
        raise click.UsageError('`--base-url` or `DEFECTDOJO_BASE_URL` is required for API commands.')
    if config.token and (config.username or config.password):
        raise click.UsageError('Provide `--token` or `--username`/`--password`, not both.')
    if bool(config.username) != bool(config.password):
        raise click.UsageError('Provide both `--username` and `--password` for basic auth.')
    if config.token is None and config.username is None:
        raise click.UsageError('Authentication is required: use `--token` or `--username`/`--password`.')

    auth = (config.username, config.password) if config.username and config.password else None
    return DefectDojo(
        base_url=config.base_url,
        token=config.token,
        auth=auth,
        verify_ssl=not config.insecure,
    )


class DojoCli(Group):
    """CLI for the DefectDojo generated API client."""

    ctx: click.Context = Context()
    base_url: Optional[str] = Option(default=_get_env('DEFECTDOJO_BASE_URL'), type=str, help='DefectDojo base URL.')
    token: Optional[str] = Option(default=_get_env('DEFECTDOJO_TOKEN'), type=str, help='DefectDojo API token.')
    username: Optional[str] = Option(default=_get_env('DEFECTDOJO_USERNAME'), type=str, help='Basic auth username.')
    password: Optional[str] = Option(default=_get_env('DEFECTDOJO_PASSWORD'), type=str, help='Basic auth password.')
    insecure: bool = Option(help='Disable TLS certificate verification.')

    def __call__(self) -> None:
        self.ctx.obj = CliConfig(
            base_url=self.base_url,
            token=self.token,
            username=self.username,
            password=self.password,
            insecure=self.insecure,
        )


class Version(DojoCli.Command, Command):
    """Print the installed package version."""

    def __call__(self) -> None:
        print(__version__)


class UserProfile(DojoCli.Command, Command):
    """Fetch the authenticated user profile."""

    class Config(Command.Config):
        name = 'user-profile'

    config: CliConfig = ContextObj()

    def __call__(self) -> None:
        payload = _build_client(self.config).user_profile_api.retrieve()
        _print_payload(payload)


class SystemSettings(DojoCli.Command, Command):
    """Fetch DefectDojo system settings."""

    class Config(Command.Config):
        name = 'system-settings'

    config: CliConfig = ContextObj()

    def __call__(self) -> None:
        payload = _build_client(self.config).system_settings_api.list()
        _print_payload(payload)


def main(argv: Optional[Sequence[str]] = None) -> int:
    return DojoCli.click.main(args=list(argv) if argv is not None else None, prog_name='defectdojo')
