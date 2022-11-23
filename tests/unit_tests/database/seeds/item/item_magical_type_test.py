from carnage.database.seeds.item import item_magical_type


def test_item_magical_type_seed_init(database_session_mock):
    seed = item_magical_type.ItemMagicalTypeSeed()

    assert seed.name is not None
    assert seed.data is not None
