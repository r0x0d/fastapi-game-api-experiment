from carnage.database.seeds import item_rarity


def test_item_rarity_seed_init(database_session_mock):
    seed = item_rarity.ItemRaritySeed()

    assert seed.name is not None
    assert seed.data is not None
