from carnage.database.repository.item import item_rarity


def test_item_rarity_repository_init(database_session_mock):
    repository = item_rarity.ItemRarityRepository()
    assert repository.session is not None
