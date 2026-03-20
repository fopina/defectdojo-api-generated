"""Command-line entrypoint for defectdojo_api_generated."""

import classyclick
import click

from defectdojo_api_generated.client import DefectDojo

from .cli import CLI


class Status(CLI.Command, classyclick.Command):
    """Quick connectivity check"""

    client: DefectDojo = classyclick.ContextMeta('client')

    def __call__(self):
        click.echo(f'Hostname: {click.style(self.client.config.host, bold=True)}')
        if self.client.config.api_key:
            click.echo('Auth: <token>')
        else:
            click.echo(f'Auth: {click.style(self.client.config.username, bold=True)} (password)')

        profile = self.client.user_profile_api.retrieve()
        click.echo(f'Confirmed connection: connected as {click.style(profile.user.username, bold=True)}')
