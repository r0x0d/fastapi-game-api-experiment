from carnage.database.repository.item import item


def test_item_repository_init(database_session_mock):
    repository = item.ItemRepository()
    assert repository.session is not None
