from carnage.database.seeds import difficulty


def test_difficulty_seed_init(database_session_mock):
    seed = difficulty.DifficultySeed()

    assert seed.name is not None
    assert seed.data is not None
