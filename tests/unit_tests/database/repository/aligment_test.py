from carnage.database.repository import aligment


def test_aligment_repository_init(database_session_mock):
    repository = aligment.AligmentRepository()
    assert repository.session is not None
