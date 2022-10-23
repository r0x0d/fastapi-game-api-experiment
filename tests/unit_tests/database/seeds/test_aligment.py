from carnage.database.seeds import aligment


def test_aligment_seed_init(database_session_mock):
    seed = aligment.AligmentSeed()

    assert seed.name is not None
    assert seed.data is not None
