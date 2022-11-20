from carnage.database.repository import account


def test_account_repository_init(database_session_mock):
    repository = account.AccountRepository()
    assert repository.session is not None


def test_select_by_username(database_session_mock):
    repository = account.AccountRepository()
    repository.select_by_username(username="test")
    assert repository.session is not None


def test_select_by_nickname(database_session_mock):
    repository = account.AccountRepository()
    repository.select_by_nickname(nickname="test")
    assert repository.session is not None
