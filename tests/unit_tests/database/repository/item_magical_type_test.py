from carnage.database.repository import item_magical_type


def test_item_magical_type_repository_init(database_session_mock):
    repository = item_magical_type.ItemMagicalTypeRepository()
    assert repository.session is not None
