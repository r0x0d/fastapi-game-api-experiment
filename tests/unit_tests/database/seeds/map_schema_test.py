from carnage.database.seeds import map_schema


def test_map_schema_seed_init(database_session_mock):
    seed = map_schema.MapSchemaSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = map_schema.MapSchemaSeed()
    seed.seed()

    for data in seed.data:
        assert "map_difficulty_id" in data
