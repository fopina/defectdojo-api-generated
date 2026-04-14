import pathlib
import re
import tomllib
import unittest

import defectdojo_api_generated


ROOT = pathlib.Path(__file__).resolve().parents[2]


class TestPackagingLayout(unittest.TestCase):
    def test_library_package_has_no_console_scripts(self):
        pyproject = tomllib.loads((ROOT / 'pyproject.toml').read_text())

        self.assertNotIn('scripts', pyproject['project'])

    def test_cli_wrapper_package_owns_console_scripts(self):
        pyproject = tomllib.loads((ROOT / 'packages' / 'cli' / 'pyproject.toml').read_text())

        self.assertEqual(
            pyproject['project']['scripts'],
            {
                'dojo': 'defectdojo_api_generated_cli.__main__:main',
                'defectdojo-api-generated': 'defectdojo_api_generated_cli.__main__:main',
            },
        )

    def test_cli_wrapper_version_matches_library_version(self):
        wrapper_init = (ROOT / 'packages' / 'cli' / 'src' / 'defectdojo_api_generated_cli' / '__init__.py').read_text()
        match = re.search(r"__version__ = '([^']+)'", wrapper_init)

        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), defectdojo_api_generated.__version__)

    def test_cli_wrapper_dependency_matches_library_version(self):
        pyproject = tomllib.loads((ROOT / 'packages' / 'cli' / 'pyproject.toml').read_text())

        self.assertIn(
            f'defectdojo-api-generated=={defectdojo_api_generated.__version__}',
            pyproject['project']['dependencies'],
        )
