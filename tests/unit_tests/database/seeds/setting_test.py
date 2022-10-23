from carnage.database.seeds import setting


def test_setting_seed_init(database_session_mock):
    seed = setting.SettingSeed()

    assert seed.name is not None
    assert seed.data is not None
