from carnage.database.seeds import account


def test_account_seed_init(database_session_mock):
    seed = account.AccountSeed()

    assert seed.name is not None
    assert seed.data is not None
