from carnage.database.repository.monster import monster


def test_monster_repository_init(database_session_mock):
    repository = monster.MonsterRepository()
    assert repository.session is not None
