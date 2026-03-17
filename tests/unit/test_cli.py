import unittest
from pathlib import Path

from defectdojo_api_generated.cli.commands.apis import API_COMMANDS
from defectdojo_api_generated.cli.commands.cli import CLI


class TestCLI(unittest.TestCase):
    def test_all_api_modules_are_registered_as_cli_commands(self):
        api_dir = Path(__file__).parents[2] / 'defectdojo_api_generated' / 'api'
        expected_modules = {path.stem for path in api_dir.glob('*_api.py') if path.name != '__init__.py'}
        expected_command_names = {
            module_name.removesuffix('_api').replace('_', '-') for module_name in expected_modules
        }

        self.assertSetEqual(set(API_COMMANDS), expected_modules)
        self.assertTrue(expected_command_names.issubset(CLI.click.commands))
