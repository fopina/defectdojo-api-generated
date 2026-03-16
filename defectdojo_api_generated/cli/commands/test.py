import classyclick

from .cli import CLI


class Version(CLI.Command, classyclick.Command):
    def __call__(self):
        print('ehlo')
