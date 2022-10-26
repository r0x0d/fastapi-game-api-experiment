from carnage.database.seeds import item_base_type


def test_item_base_type_seed_init(database_session_mock):
    seed = item_base_type.ItemBaseTypeSeed()

    assert seed.name is not None
    assert seed.data is not None
