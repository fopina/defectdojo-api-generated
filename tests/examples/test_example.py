import sys
from io import StringIO
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase, mock


class Test(TestCase):
    def test_example(self) -> None:

        sys.path.append(Path(__file__).resolve().parents[2])

        import example

        dojo = mock.Mock()
        dojo.findings_api.list_iterator.return_value = [
            SimpleNamespace(
                page=SimpleNamespace(count=2),
                result=SimpleNamespace(
                    severity='High',
                    title='Stored XSS',
                    description='First finding',
                ),
            ),
            SimpleNamespace(
                page=SimpleNamespace(count=2),
                result=SimpleNamespace(
                    severity='Medium',
                    title='Stored XSS',
                    description='Second finding',
                ),
            ),
        ]
        dojo.system_settings_api.list.return_value = SimpleNamespace(results=['setting'])

        stdout = StringIO()
        with (
            mock.patch('defectdojo_api_generated.DefectDojo', return_value=dojo) as defect_dojo_cls,
            mock.patch('sys.stdout', new=stdout),
        ):
            example.main()

        defect_dojo_cls.assert_called_once_with(
            base_url='https://demo.defectdojo.org/',
            auth=('admin', example.PASSWORD),
        )
        dojo.findings_api.list_iterator.assert_called_once_with(title='Stored XSS')
        dojo.system_settings_api.list.assert_called_once_with(limit=1)
        self.assertEqual(
            stdout.getvalue(),
            '\n'.join(
                [
                    'Total matched findings: 2',
                    '- [High] Stored XSS - First finding',
                    '- [Medium] Stored XSS - Second finding',
                    '- setting',
                    '',
                ]
            ),
        )
