from carnage.database.repository.vocation import vocation


def test_vocation_repository_init(database_session_mock):
    repository = vocation.VocationRepository()
    assert repository.session is not None
