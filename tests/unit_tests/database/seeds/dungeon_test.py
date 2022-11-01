from carnage.database.seeds.dungeon import dungeon


def test_dungeon_seed_init(database_session_mock):
    seed = dungeon.DungeonSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = dungeon.DungeonSeed()
    seed.seed()

    for data in seed.data:
        assert "dungeon_schema_id" in data
