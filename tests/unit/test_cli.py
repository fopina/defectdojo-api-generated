import json
import sys
import unittest
from pathlib import Path
from typing import Optional
from unittest import mock

from click.testing import CliRunner
from pydantic import Field
from typing_extensions import Annotated

from defectdojo_api_generated.api.findings_api import FindingsApi
from defectdojo_api_generated.api.products_api import ProductsApi
from defectdojo_api_generated.cli.commands.apis import make_api_group
from defectdojo_api_generated.cli.commands.cli import CLI
from defectdojo_api_generated.cli.commands.config import Config as _ConfigCommand
from defectdojo_api_generated.exceptions import BadRequestException
from defectdojo_api_generated.helpers import IteratorResult


class TestCLI(unittest.TestCase):
    def _register_test_api_group(self, module_name: str, api_class: type) -> None:
        group = make_api_group(module_name, api_class)
        CLI.click.commands['api'].add_command(group.click)

    def test_findings_list_command_runs(self):
        self.assertIn('findings', CLI.click.commands['api'].commands)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'findings', '--help'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('Usage: cli api findings', result.output)
        self.assertIn('methods from `FindingsApi`.', result.output)

    def test_api_commands_capture_their_own_method(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with (
                mock.patch.object(FindingsApi, 'list_iterator', new=lambda self: 'list-result'),
                mock.patch.object(
                    FindingsApi,
                    'create',
                    new=lambda self, finding_create_request, **kwargs: finding_create_request.title,
                ),
            ):
                list_result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'findings', 'list'])
                create_result = runner.invoke(
                    CLI.click,
                    [
                        '--config',
                        str(config_path),
                        'api',
                        'findings',
                        'create',
                        '--title',
                        'create-result',
                    ],
                )

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
                result = runner.invoke(
                    CLI.click,
                    ['--config', str(config_path), 'api', 'findings', 'list', '--limit', '1'],
                )

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
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'findings', 'list'])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.splitlines(), ['first', '', '---', '', 'second'])

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
                result = runner.invoke(
                    CLI.click,
                    ['--config', str(config_path), 'api', 'findings', 'list', '--json'],
                )

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
                        ['--config', str(config_path), 'api', 'findings', 'list', '--jq', 'title'],
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
                        ['--config', str(config_path), 'api', 'findings', 'list', '--json', '--jq', 'title'],
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

        self._register_test_api_group('docstring_api', DocstringApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'docstring', '--help'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('Fetch a single item.', result.output)
        self.assertNotIn('`fetch`.', result.output)

    def test_iterator_command_help_falls_back_to_base_method_docstring(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'findings', 'list', '--help'])

        self.assertEqual(result.exit_code, 0)
        self.assertNotIn('`list_iterator`.', result.output)

    def test_annotated_method_parameters_become_options(self):
        class AnnotatedApi:
            def __init__(self, api_client):
                self.api_client = api_client

            def fetch(self, limit: Annotated[int, Field(description='How many items to return')] = 10):
                return f'limit={limit}'

        self._register_test_api_group('annotated_api', AnnotatedApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            help_result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'annotated', '--help'])
            run_result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'annotated', '--limit', '7'])

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

        self._register_test_api_group('internal_param_api', InternalParamApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            help_result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'internal-param', '--help'])

        self.assertEqual(help_result.exit_code, 0)
        self.assertIn('--limit', help_result.output)
        self.assertNotIn('_request_timeout', help_result.output)

    def test_non_primitive_parameters_raise_type_error(self):
        class NonPrimitiveApi:
            def __init__(self, api_client):
                self.api_client = api_client

            def fetch(self, payload: Optional[dict[str, str]] = None):
                return payload

        with self.assertRaisesRegex(TypeError, 'dict\\[str, str\\]'):
            make_api_group('non_primitive_api', NonPrimitiveApi)

    def test_required_request_body_parameters_become_field_flags(self):
        command = CLI.click.commands['api'].commands['products'].commands['create']
        option = next(param for param in command.params if getattr(param, 'name', None) == 'name')
        self.assertFalse(any(getattr(param, 'name', None) == 'product_request' for param in command.params))
        self.assertEqual(option.required, False)
        self.assertEqual(option.type.name, 'text')

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch.object(
                ProductsApi,
                'create',
                new=lambda self, product_request, **kwargs: product_request.model_dump(),
            ):
                run_result = runner.invoke(
                    CLI.click,
                    [
                        '--config',
                        str(config_path),
                        'api',
                        'products',
                        'create',
                        '--name',
                        'Example',
                        '--json',
                    ],
                )

        self.assertEqual(run_result.exit_code, 0)
        payload = json.loads(run_result.output)
        self.assertEqual(payload['name'], 'Example')

    def test_bad_request_exception_uses_detail_message(self):
        runner = CliRunner()

        def raise_bad_request(self, product_request, **kwargs):
            raise BadRequestException(
                status=400,
                body='{"detail":"Invalid product"}',
                data={'detail': 'Invalid product'},
            )

        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch.object(
                ProductsApi,
                'create',
                new=raise_bad_request,
            ):
                result = runner.invoke(
                    CLI.click,
                    [
                        '--config',
                        str(config_path),
                        'api',
                        'products',
                        'create',
                        '--name',
                        'Example',
                    ],
                )

        self.assertEqual(result.exit_code, 1)
        self.assertIn('Error: Invalid product', result.output)
        self.assertNotIn('BadRequestException', result.output)

    def test_single_letter_parameters_use_short_options_only(self):
        command = CLI.click.commands['api'].commands['findings'].commands['list']
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

        self._register_test_api_group('single_method_api', SingleMethodApi)

        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with mock.patch('defectdojo_api_generated.cli.commands.cli.DefectDojo') as defectdojo:
                defectdojo.return_value = mock.Mock(api_client=object())
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'api', 'single-method'])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), 'pong')

    def test_config_command_masks_secret_fields(self):
        self.assertIsNotNone(_ConfigCommand)
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text(
                '\n'.join(
                    [
                        "default_env = 'demo'",
                        "host = 'https://example.com'",
                        "user = 'root-user'",
                        "password = 'root-password'",
                        '',
                        '[env.demo]',
                        "token = 'super-secret-token'",
                        'disable_tls = true',
                    ]
                )
            )

            with mock.patch('defectdojo_api_generated.cli.commands.cli.DefectDojo') as defectdojo:
                defectdojo.return_value = mock.Mock(config=mock.Mock())
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'config'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('Config file:', result.output)
        self.assertIn('Environment: demo', result.output)
        self.assertIn('"host": "https://example.com"', result.output)
        self.assertIn('"user": "root-user"', result.output)
        self.assertIn('"token": "<masked>"', result.output)
        self.assertIn('"password": "<masked>"', result.output)
        self.assertNotIn('super-secret-token', result.output)
        self.assertNotIn('root-password', result.output)

    def test_config_command_edit_uses_editor_env(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with (
                mock.patch('defectdojo_api_generated.cli.commands.cli.DefectDojo') as defectdojo,
                mock.patch.dict('os.environ', {'EDITOR': 'vim -f'}, clear=False),
                mock.patch('defectdojo_api_generated.cli.commands.config.subprocess.run') as run_mock,
            ):
                defectdojo.return_value = mock.Mock(config=mock.Mock())
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'config', '--edit'])

        self.assertEqual(result.exit_code, 0)
        run_mock.assert_called_once_with(['vim', '-f', str(config_path)], check=True)

    def test_config_command_edit_falls_back_to_first_available_editor(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with (
                mock.patch('defectdojo_api_generated.cli.commands.cli.DefectDojo') as defectdojo,
                mock.patch.dict('os.environ', {}, clear=True),
                mock.patch('defectdojo_api_generated.cli.commands.config.shutil.which') as which_mock,
                mock.patch('defectdojo_api_generated.cli.commands.config.subprocess.run') as run_mock,
            ):
                defectdojo.return_value = mock.Mock(config=mock.Mock())
                which_mock.side_effect = [None, '/usr/bin/vi', '/usr/bin/nano']
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'config', '--edit'])

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(which_mock.call_args_list, [mock.call('vim'), mock.call('vi')])
        run_mock.assert_called_once_with(['vi', str(config_path)], check=True)

    def test_config_command_edit_requires_configured_or_installed_editor(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            config_path = Path('config.toml')
            config_path.write_text("host = 'https://example.com'\ntoken = 'token'\n")

            with (
                mock.patch('defectdojo_api_generated.cli.commands.cli.DefectDojo') as defectdojo,
                mock.patch.dict('os.environ', {}, clear=True),
                mock.patch('defectdojo_api_generated.cli.commands.config.shutil.which', return_value=None),
            ):
                defectdojo.return_value = mock.Mock(config=mock.Mock())
                result = runner.invoke(CLI.click, ['--config', str(config_path), 'config', '--edit'])

        self.assertEqual(result.exit_code, 1)
        self.assertIn('No editor configured. Set VISUAL or EDITOR, or install vim, vi, or nano.', result.output)
