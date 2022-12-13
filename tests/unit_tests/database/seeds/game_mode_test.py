from carnage.database.seeds import game_mode


def test_game_mode_seed_init(database_session_mock):
    seed = game_mode.GameModeSeed()

    assert seed.name is not None
    assert seed.data is not None
