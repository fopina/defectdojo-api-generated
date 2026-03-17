import unittest
from importlib.metadata import version
from pathlib import Path

from click.testing import CliRunner

from defectdojo_api_generated.cli.commands.apis import API_COMMANDS
from defectdojo_api_generated.cli.commands.cli import CLI


class TestCLI(unittest.TestCase):
    def test_findings_list_command_runs(self):
        self.assertIn('findings_api', API_COMMANDS)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            result = runner.invoke(CLI.click)

        click_version = tuple(int(part) for part in version('click').split('.')[:2])
        expected_exit_code = 2 if click_version >= (8, 2) else 0
        self.assertEqual(result.exit_code, expected_exit_code)
        self.assertRegex(result.output, r'findings\s+`FindingsApi`\.')
