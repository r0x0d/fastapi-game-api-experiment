from carnage.database.repository.monster import monster_type


def test_monster_type_repository_init(database_session_mock):
    repository = monster_type.MonsterTypeRepository()
    assert repository.session is not None
