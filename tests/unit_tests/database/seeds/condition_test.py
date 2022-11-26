from carnage.database.seeds import condition


def test_condition_seed_init(database_session_mock):
    seed = condition.ConditionSeed()

    assert seed.name is not None
    assert seed.data is not None
