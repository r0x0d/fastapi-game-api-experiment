from carnage.database.repository import account


def test_account_repository_init(database_session_mock):
    repository = account.AccountRepository()
    assert repository.session is not None
