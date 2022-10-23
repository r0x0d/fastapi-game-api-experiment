from carnage.database.repository import setting


def test_setting_repository_init(database_session_mock):
    repository = setting.SettingRepository()
    assert repository.session is not None
