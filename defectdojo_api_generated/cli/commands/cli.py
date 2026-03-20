"""Command-line entrypoint for defectdojo_api_generated."""

import logging
from pathlib import Path
from typing import Optional

import classyclick
import click
from platformdirs import user_config_dir

from defectdojo_api_generated.client import DefectDojo

from ... import __version__

try:
    # Python 3.11+
    import tomllib
except ModuleNotFoundError:
    # Python < 3.11
    import tomli as tomllib  # type: ignore


DEFAULT_PATH = Path(user_config_dir('defectdojo-generated-api')) / 'config.toml'


def ensure_config_file(config_path: Optional[Path]) -> Path:
    config_path = config_path or DEFAULT_PATH
    if not config_path.exists():
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text((Path(__file__).parent.parent / 'config.example.toml').read_text())
        print(f'Info: No configuration file found at {config_path}, a sample config has been placed there.')

    return config_path


def load_config_data(config_path: Path) -> dict:
    with config_path.open('rb') as f:
        return tomllib.load(f)


class CLI(classyclick.Group):
    """DefectDojo CLI"""

    __config__ = classyclick.Group.Config(context_settings=dict(show_default=True))

    config: Path = classyclick.Option(help='Path to the configuration file', show_default=str(DEFAULT_PATH))
    env: str = classyclick.Option(
        '-e', help='Environment to use for the command (as many can be specified in config.toml)'
    )
    host: str = classyclick.Option(
        '-h',
        envvar='DEFECTDOJO_HOST',
        show_envvar=True,
        help='DefectDojo server host',
    )
    token: str = classyclick.Option(
        '-t',
        envvar='DEFECTDOJO_TOKEN',
        show_envvar=True,
        help='DefectDojo API token - if provided, --user/--password are ignored',
    )
    user: str = classyclick.Option(
        '-u',
        envvar='DEFECTDOJO_USER',
        show_envvar=True,
        help='DefectDojo API username',
    )
    password: str = classyclick.Option(
        '-p',
        envvar='DEFECTDOJO_PASSWORD',
        show_envvar=True,
        help='DefectDojo API password',
    )
    disable_tls: bool = classyclick.Option(help='Disable TLS verification in DefectDojo API requests')
    debug_http: bool = classyclick.Option(help='Log HTTP requests and responses')
    ctx: classyclick.Context = classyclick.Context()

    def __call__(self):
        self.config = ensure_config_file(self.config)
        config_data = load_config_data(self.config)

        if self.env is None:
            self.env = config_data.get('default_env')

        # allow empty string to choose root environment when "default_env" is set to something else
        if self.env:
            if self.env not in config_data.get('env', {}):
                raise click.ClickException(f'Environment "{self.env}" not found in {self.config}')
            env_config = config_data['env'][self.env]
            config_data = merge_dicts(config_data, env_config)

        # to late to have these options from default_map, so process them manually
        if self.host is None:
            self.host = config_data.get('host')

        if self.token is None:
            self.token = config_data.get('token')

        if self.user is None:
            self.user = config_data.get('user')

        if self.password is None:
            self.password = config_data.get('password')

        if self.disable_tls is None:
            self.disable_tls = config_data.get('disable_tls', False)

        if self.debug_http:
            import http.client

            http.client.HTTPConnection.debuglevel = 1
            http.client.HTTPSConnection.debuglevel = 1
            logging.basicConfig(level=logging.DEBUG)
            http_client_logger = logging.getLogger('http.client')
            http_client_logger.setLevel(logging.DEBUG)

        self.ctx.meta['client'] = DefectDojo(
            base_url=self.host,
            token=self.token,
            auth=None if self.token else (self.user, self.password),
            verify_ssl=not self.disable_tls,
        )
        self.ctx.meta['config_path'] = self.config
        self.ctx.meta['config_data'] = config_data
        self.ctx.meta['selected_env'] = self.env

        self.ctx.default_map = config_data


def merge_dicts(base: dict, override: dict) -> dict:
    """
    To merge two Python dictionaries where:
    * nested dictionaries should merge recursively
    * lists and other values should be replaced entirely

    by ChatGPT
    """
    result = base.copy()
    for key, value in override.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            else:
                result[key] = value
        else:
            result[key] = value
    return result


# TODO: classyclick missing @click.version_option - https://github.com/fopina/classyclick/issues/48
CLI.click = click.version_option(version=__version__, message='%(version)s')(CLI.click)
