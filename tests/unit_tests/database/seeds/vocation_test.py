from carnage.database.seeds import vocation


def test_vocation_seed_init(database_session_mock):
    seed = vocation.VocationSeed()

    assert seed.name is not None
    assert seed.data is not None
