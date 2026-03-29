import classyclick

from .cli import CLI


class Config(classyclick.helpers.ConfigBaseCommand, CLI.Command):
    pass
