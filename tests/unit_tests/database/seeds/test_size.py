from carnage.database.seeds import size


def test_size_seed_init(database_session_mock):
    seed = size.SizeSeed()

    assert seed.name is not None
    assert seed.data is not None
