from carnage.database.seeds import item


def test_item_seed_init(database_session_mock):
    seed = item.ItemSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = item.ItemSeed()
    seed.seed()

    for data in seed.data:
        assert "item_rarity_id" in data
        assert "item_base_type_id" in data
        assert "item_magical_type_id" in data
