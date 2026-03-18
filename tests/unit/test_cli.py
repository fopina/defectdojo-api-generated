import json
import sys
import unittest
from importlib.metadata import version
from pathlib import Path
from unittest import mock

from click.testing import CliRunner
from pydantic import Field
from typing_extensions import Annotated

from defectdojo_api_generated.api.findings_api import FindingsApi
from defectdojo_api_generated.cli.commands.apis import API_COMMANDS, make_api_group
from defectdojo_api_generated.cli.commands.cli import CLI
from defectdojo_api_generated.helpers import IteratorResult


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
        self.assertRegex(result.output, r'findings\s+methods from `FindingsApi`\.')

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

    def test_findings_list_accepts_limit_option(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch.object(FindingsApi, 'list_iterator', new=lambda self, **kwargs: kwargs):
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'list', '--limit', '1'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('limit: 1', result.output)

    def test_findings_list_prints_iterator_items_one_per_line(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch.object(
                FindingsApi,
                'list_iterator',
                new=lambda self, **kwargs: [
                    IteratorResult(result='first', page='page-1'),
                    IteratorResult(result='second', page='page-2'),
                ],
            ):
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'list'])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.splitlines(), ['first', '---', 'second'])

    def test_json_flag_dumps_json_output(self):
        from defectdojo_api_generated.models.finding import Finding

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch.object(
                FindingsApi,
                'list_iterator',
                new=lambda self, **kwargs: [IteratorResult(result=Finding(id=1, title='Example'), page='page-1')],
            ):
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'findings', 'list', '--json'])

        self.assertEqual(result.exit_code, 0)
        payload = json.loads(result.output)
        self.assertEqual(payload['id'], 1)
        self.assertEqual(payload['title'], 'Example')
        self.assertIn('accepted_risks', payload)

    def test_jq_flag_projects_text_output(self):
        from defectdojo_api_generated.models.finding import Finding

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            fake_jmespath = mock.Mock(search=lambda expression, data: data['title'])
            with mock.patch.dict(sys.modules, {'jmespath': fake_jmespath}):
                with mock.patch.object(
                    FindingsApi,
                    'list_iterator',
                    new=lambda self, **kwargs: [IteratorResult(result=Finding(id=1, title='Example'), page='page-1')],
                ):
                    result = runner.invoke(
                        CLI.click,
                        ['--config', str(config_path), 'findings', 'list', '--jq', 'title'],
                    )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), 'Example')

    def test_jq_flag_projects_json_output(self):
        from defectdojo_api_generated.models.finding import Finding

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            fake_jmespath = mock.Mock(search=lambda expression, data: data['title'])
            with mock.patch.dict(sys.modules, {'jmespath': fake_jmespath}):
                with mock.patch.object(
                    FindingsApi,
                    'list_iterator',
                    new=lambda self, **kwargs: [IteratorResult(result=Finding(id=1, title='Example'), page='page-1')],
                ):
                    result = runner.invoke(
                        CLI.click,
                        ['--config', str(config_path), 'findings', 'list', '--json', '--jq', 'title'],
                    )

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(json.loads(result.output), 'Example')

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

    def test_annotated_method_parameters_become_options(self):
        class AnnotatedApi:
            def __init__(self, api_client):
                self.api_client = api_client

            def fetch(self, limit: Annotated[int, Field(description='How many items to return')] = 10):
                return f'limit={limit}'

        make_api_group('annotated_api', AnnotatedApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            help_result = runner.invoke(CLI.click, ['--config', str(config_path), 'annotated', '--help'])
            run_result = runner.invoke(CLI.click, ['--config', str(config_path), 'annotated', '--limit', '7'])

        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--limit', help_result.output)
        self.assertIn('How many items to return', help_result.output)
        self.assertEqual(run_result.exit_code, 0)
        self.assertEqual(run_result.output.strip(), 'limit=7')

    def test_internal_method_parameters_are_skipped(self):
        class InternalParamApi:
            def __init__(self, api_client):
                self.api_client = api_client

            def fetch(self, limit: int = 10, _request_timeout: int = 5):
                return f'limit={limit}'

        make_api_group('internal_param_api', InternalParamApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            help_result = runner.invoke(CLI.click, ['--config', str(config_path), 'internal-param', '--help'])

        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--limit', help_result.output)
        self.assertNotIn('_request_timeout', help_result.output)

    def test_single_letter_parameters_use_short_options_only(self):
        command = API_COMMANDS['findings_api'].click.commands['list']
        option = next(param for param in command.params if getattr(param, 'name', None) == 'o')

        self.assertEqual(option.opts, ['-o'])
        self.assertEqual(option.secondary_opts, [])

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
