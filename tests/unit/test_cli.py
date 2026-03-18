import unittest
from importlib.metadata import version
from pathlib import Path
from unittest import mock

from click.testing import CliRunner

from defectdojo_api_generated.api.findings_api import FindingsApi
from defectdojo_api_generated.cli.commands.apis import API_COMMANDS, make_api_group
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

    def test_api_commands_capture_their_own_method(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with (
                mock.patch.object(FindingsApi, 'list_iterator', new=lambda self: 'list-result'),
                mock.patch.object(FindingsApi, 'create', new=lambda self: 'create-result'),
            ):
                list_result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'list'])
                create_result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'create'])

        self.assertEqual(list_result.exit_code, 0)
        self.assertEqual(create_result.exit_code, 0)
        self.assertEqual(list_result.output.strip(), 'list-result')
        self.assertEqual(create_result.output.strip(), 'create-result')

    def test_api_command_help_uses_method_docstring(self):
        class DocstringApi:
            def __init__(self, api_client):
                self.api_client = api_client

            def fetch(self):
                """Fetch a single item."""
                return 'ok'

        make_api_group('docstring_api', DocstringApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            result = runner.invoke(CLI.click, ['--config', str(config_path), 'docstring', '--help'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('Fetch a single item.', result.output)
        self.assertNotIn('`fetch`.', result.output)

    def test_iterator_command_help_falls_back_to_base_method_docstring(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'list', '--help'])

        self.assertEqual(result.exit_code, 0)
        self.assertNotIn('`list_iterator`.', result.output)

    def test_single_method_api_becomes_direct_command(self):
        class SingleMethodApi:
            def __init__(self, api_client):
                self.api_client = api_client

            def ping(self):
                return 'pong'

            def ping_with_http_info(self):
                raise AssertionError('should be filtered out')

        make_api_group('single_method_api', SingleMethodApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch('defectdojo_api_generated.cli.commands.cli.DefectDojo') as defectdojo:
                defectdojo.return_value = mock.Mock(api_client=object())
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'single-method'])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), 'pong')
