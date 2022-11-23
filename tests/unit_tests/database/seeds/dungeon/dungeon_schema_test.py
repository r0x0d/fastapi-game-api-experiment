from carnage.database.seeds.dungeon import dungeon_schema


def test_dungeon_schema_seed_init(database_session_mock):
    seed = dungeon_schema.DungeonSchemaSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = dungeon_schema.DungeonSchemaSeed()
    seed.seed()

    for data in seed.data:
        assert "dungeon_difficulty_id" in data
