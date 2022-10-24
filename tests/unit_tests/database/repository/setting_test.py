from carnage.database.repository import setting


def test_setting_repository_init(database_session_mock):
    repository = setting.SettingRepository()
    assert repository.session is not None


def test_select_by_environment(database_session_mock):
    repository = setting.SettingRepository()
    repository.select_by_environment()
    assert repository.session is not None
