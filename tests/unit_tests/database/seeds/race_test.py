from carnage.database.seeds import race


def test_race_seed_init(database_session_mock):
    seed = race.RaceSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = race.RaceSeed()
    seed.seed()

    for data in seed.data:
        assert "aligment_id" in data
        assert "size_id" in data
