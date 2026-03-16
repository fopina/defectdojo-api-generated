import pytest

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


def test_version_command(capsys):
    assert cli.main(['version']) == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == __version__


def test_user_profile_command(monkeypatch, capsys):
    monkeypatch.setattr(cli, 'DefectDojo', lambda **kwargs: DummyClient())

    assert (
        cli.main(
            [
                '--base-url',
                'https://demo.defectdojo.org/',
                '--token',
                'secret',
                'user-profile',
            ]
        )
        == 0
    )

    captured = capsys.readouterr()
    assert '"username": "alice"' in captured.out


def test_api_commands_require_auth():
    with pytest.raises(SystemExit) as exc:
        cli.main(['--base-url', 'https://demo.defectdojo.org/', 'user-profile'])

    assert exc.value.code == 2
