from carnage.database.repository import map


def test_map_repository_init(database_session_mock):
    repository = map.MapRepository()
    assert repository.session is not None
