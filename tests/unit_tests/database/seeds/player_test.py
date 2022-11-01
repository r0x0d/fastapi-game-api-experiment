from carnage.database.seeds import player


def test_player_seed_init(database_session_mock):
    seed = player.PlayerSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = player.PlayerSeed()
    seed.seed()

    for data in seed.data:
        assert "dungeon_id" in data
        assert "vocation_id" in data
