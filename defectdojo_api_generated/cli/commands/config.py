"""Configuration inspection and editing command."""

import json
import os
import shlex
import subprocess

import classyclick
import click

from .cli import CLI

_MASKED = '<masked>'
_SECRET_FIELD_PARTS = ('token', 'password')


def _mask_value(key: str, value):
    if isinstance(value, dict):
        return {nested_key: _mask_value(nested_key, nested_value) for nested_key, nested_value in value.items()}

    if isinstance(value, list):
        return [_mask_value(key, item) for item in value]

    if value is None:
        return None

    if any(part in key.lower() for part in _SECRET_FIELD_PARTS):
        return _MASKED

    return value


def _resolve_editor() -> str:
    editor = os.environ.get('VISUAL') or os.environ.get('EDITOR')
    if not editor:
        raise click.ClickException('No editor configured. Set VISUAL or EDITOR.')

    return editor


class Config(CLI.Command, classyclick.Command):
    """Show or edit the current CLI configuration"""

    edit: bool = classyclick.Option('-e', help='Open the config file in $VISUAL or $EDITOR')

    def __call__(self):
        ctx = click.get_current_context().find_root()
        config_path = ctx.meta['config_path']

        if self.edit:
            editor = _resolve_editor()
            try:
                subprocess.run([*shlex.split(editor), str(config_path)], check=True)
            except FileNotFoundError as exc:
                raise click.ClickException(f'Editor command not found: {editor}') from exc
            except subprocess.CalledProcessError as exc:
                raise click.ClickException(f'Editor exited with status {exc.returncode}') from exc
            return

        config = {key: value for key, value in ctx.meta['config_data'].items() if key != 'env'}

        click.echo(f'Config file: {click.style(str(config_path), bold=True)}')
        if ctx.meta['selected_env']:
            click.echo(f'Environment: {click.style(ctx.meta["selected_env"], bold=True)}')

        click.echo(json.dumps(_mask_value('config', config), indent=2, sort_keys=True))
