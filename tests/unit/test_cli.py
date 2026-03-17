import unittest
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

            result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'list'])

        self.assertEqual(result.exit_code, 0, result.output)
