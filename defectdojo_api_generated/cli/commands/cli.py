"""Command-line entrypoint for defectdojo_api_generated."""

import logging
from pathlib import Path

import classyclick
import click

from defectdojo_api_generated.client import DefectDojo

from ... import __version__


class CLI(classyclick.helpers.ConfigFileMixin, classyclick.Group):
    """DefectDojo CLI"""

    __config__ = classyclick.Group.Config(context_settings=dict(show_default=True))
    CONFIG_DEFAULT_NAME = 'defectdojo-generated-api'
    CONFIG_EXAMPLE_PATH = Path(__file__).parent.parent / 'config.example.toml'

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

    def __call__(self):
        self.load_config()

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


# TODO: classyclick missing @click.version_option - https://github.com/fopina/classyclick/issues/48
CLI.click = click.version_option(version=__version__, message='%(version)s')(CLI.click)

classyclick.helpers.discover_commands(__package__)
