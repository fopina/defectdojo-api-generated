import pathlib
import unittest

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    import tomli as tomllib

import defectdojo_api_generated

ROOT = pathlib.Path(__file__).resolve().parents[2]


class TestPackagingLayout(unittest.TestCase):
    def test_library_package_has_no_console_scripts(self):
        pyproject = tomllib.loads((ROOT / 'pyproject.toml').read_text())

        self.assertNotIn('scripts', pyproject['project'])

    def test_cli_distribution_points_console_scripts_to_library_entrypoint(self):
        pyproject = tomllib.loads((ROOT / 'packages' / 'cli' / 'pyproject.toml').read_text())

        self.assertEqual(
            pyproject['project']['scripts'],
            {
                'dojo': 'defectdojo_api_generated.cli.__main__:main',
                'defectdojo-api-generated-cli': 'defectdojo_api_generated.cli.__main__:main',
            },
        )

    def test_cli_distribution_version_matches_library_version(self):
        pyproject = tomllib.loads((ROOT / 'packages' / 'cli' / 'pyproject.toml').read_text())

        self.assertEqual(pyproject['project']['version'], defectdojo_api_generated.__version__)

    def test_cli_distribution_dependency_matches_library_version(self):
        pyproject = tomllib.loads((ROOT / 'packages' / 'cli' / 'pyproject.toml').read_text())

        self.assertIn(
            f'defectdojo-api-generated=={defectdojo_api_generated.__version__}',
            pyproject['project']['dependencies'],
        )
