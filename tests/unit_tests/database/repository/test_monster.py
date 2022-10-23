from carnage.database.repository import monster


def test_monster_repository_init(database_session_mock):
    repository = monster.MonsterRepository()
    assert repository.session is not None
