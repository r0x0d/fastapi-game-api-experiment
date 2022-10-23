from carnage.database.seeds import monster


def test_monster_seed_init(database_session_mock):
    seed = monster.MonsterSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = monster.MonsterSeed()
    seed.seed()

    for data in seed.data:
        assert "aligment_id" in data
        assert "size_id" in data
        assert "monster_type_id" in data
