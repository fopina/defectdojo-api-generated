from click.testing import CliRunner

from defectdojo_api_generated import __version__, cli


class DummyPayload:
    def __init__(self, data):
        self.data = data

    def model_dump(self, by_alias=True, exclude_none=True):
        return self.data


class DummyClient:
    class UserProfileApi:
        @staticmethod
        def retrieve():
            return DummyPayload({'username': 'alice'})

    class SystemSettingsApi:
        @staticmethod
        def list():
            return DummyPayload({'count': 1, 'results': [{'id': 1}]})

    user_profile_api = UserProfileApi()
    system_settings_api = SystemSettingsApi()


def test_version_command():
    result = CliRunner().invoke(cli.DojoCli.click, ['version'])
    assert result.exit_code == 0
    assert result.output.strip() == __version__


def test_user_profile_command(monkeypatch):
    monkeypatch.setattr(cli, 'DefectDojo', lambda **kwargs: DummyClient())

    result = CliRunner().invoke(
        cli.DojoCli.click,
        [
            '--base-url',
            'https://demo.defectdojo.org/',
            '--token',
            'secret',
            'user-profile',
        ],
    )

    assert result.exit_code == 0
    assert '"username": "alice"' in result.output


def test_api_commands_require_auth():
    result = CliRunner().invoke(
        cli.DojoCli.click,
        ['--base-url', 'https://demo.defectdojo.org/', 'user-profile'],
    )

    assert result.exit_code == 2
    assert 'Authentication is required' in result.output
