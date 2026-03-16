"""Command-line entrypoint for defectdojo_api_generated."""

import logging
from pathlib import Path

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
    import tomli as tomllib

DEFAULT_PATH = Path(user_config_dir('defectdojo-cli')) / 'config.toml'


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
    user: str = classyclick.Option(
        '-p',
        envvar='DEFECTDOJO_PASSWORD',
        show_envvar=True,
        help='DefectDojo API password',
    )
    disable_tls: bool = classyclick.Option(help='Disable TLS verification in DefectDojo API requests')
    debug_http: bool = classyclick.Option(help='Log HTTP requests and responses')
    ctx: classyclick.Context = classyclick.Context()

    def __call__(self):
        config = self.config
        if config is None:
            config = DEFAULT_PATH
            if not config.exists():
                config.parent.mkdir(parents=True, exist_ok=True)
                config.write_text((Path(__file__).parent.parent / 'config.example.toml').read_text())
                print(f'Info: No configuration file found at {config}, a sample config has been placed there.')

        with config.open('rb') as f:
            config_data = tomllib.load(f)

        env = self.env
        if env is None:
            env = config_data.get('default_env')

        # allow empty string to choose root environment when "default_env" is set to something else
        if env:
            if env not in config_data.get('env', {}):
                raise click.ClickException(f'Environment "{env}" not found in {config}')
            env_config = config_data['env'][env]
            config_data = merge_dicts(config_data, env_config)

        # to late to have these options from default_map, so process them manually
        host = self.host
        if host is None:
            host = config_data.get('host')

        token = self.token
        if token is None:
            token = config_data.get('token')

        disable_tls = self.disable_tls
        if disable_tls is None:
            disable_tls = config_data.get('disable_tls', False)

        debug_http = self.debug_http
        if debug_http:
            import http.client

            http.client.HTTPConnection.debuglevel = 1
            http.client.HTTPSConnection.debuglevel = 1
            logging.basicConfig(level=logging.DEBUG)
            http_client_logger = logging.getLogger('http.client')
            http_client_logger.setLevel(logging.DEBUG)

        self.ctx.meta['client'] = DefectDojo(
            base_url=host,
            token=token,
            verify_ssl=not disable_tls,
        )

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
