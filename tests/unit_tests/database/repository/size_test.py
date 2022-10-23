from carnage.database.repository import size


def test_size_repository_init(database_session_mock):
    repository = size.SizeRepository()
    assert repository.session is not None
