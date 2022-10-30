from carnage.database.seeds.map import map


def test_map_seed_init(database_session_mock):
    seed = map.MapSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = map.MapSeed()
    seed.seed()

    for data in seed.data:
        assert "map_schema_id" in data
