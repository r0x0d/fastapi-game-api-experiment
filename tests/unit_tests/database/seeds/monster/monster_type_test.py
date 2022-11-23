from carnage.database.seeds.monster import monster_type


def test_monster_type_seed_init(database_session_mock):
    seed = monster_type.MonsterTypeSeed()

    assert seed.name is not None
    assert seed.data is not None
