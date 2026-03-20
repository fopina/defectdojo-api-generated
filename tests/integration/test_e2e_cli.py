import json as _json
import uuid
from pathlib import Path

from click.testing import CliRunner

from defectdojo_api_generated.cli import __main__

from . import E2ETestCase

DATA_DIR = Path(__file__).parent.parent / 'data'


class Test(E2ETestCase):
    # Run `run_dojo.sh` manually (and stop after), set this one to True and then you can run individual tests here quickly
    _PARTIAL_RUN = False

    @classmethod
    def setUpClass(cls):
        __main__.discover_commands()
        cls.CLI = __main__.load_cli()
        super().setUpClass()

    def setUp(self):
        self.runner = CliRunner()

    def _run_cli(self, *args):
        return self.runner.invoke(
            self.CLI.click, ['--config', Path(__file__).parent / 'config.integration.toml', *args]
        )

    def test_product_types_list(self):
        self.maxDiff = None
        res = self._run_cli('product-types', 'list', '--name', 'Research and Development')
        self.assertEqual(
            res.output,
            """\
id: 1
name: Research and Development
critical_product: True
key_product: False
members: [1]
authorization_groups: []
""",
        )

    def _create_product(self, json=False):
        uniq = str(uuid.uuid4())
        args = ['products', 'create', '--prod-type', '1', '--name', f'Product Test {uniq}', '--description', 'e2e test']
        if json:
            args.append('--json')
        res = self._run_cli(*args)
        self.assertEqual(res.exit_code, 0, str(res.exception) + res.output)
        if json:
            return _json.loads(res.output)
        return res

    def test_create_product(self):
        res = self._create_product()
        self.assertIn('description: e2e test', res.output)

    def test_reimport_scan(self):
        product = self.skip_if_fail(self._create_product, json=True)
        res = self._run_cli(
            'reimport-scan',
            '--product-name',
            product['name'],
            '--engagement-name',
            'e2e-test',
            '--auto-create-context',
            '--scan-type',
            'Semgrep JSON Report',
            '--file',
            str(DATA_DIR / 'semgrep_report.json'),
        )
        self.assertEqual(res.exit_code, 0, str(res.exception) + res.output)
        self.assertIn('minimum_severity: Info', res.output)
