from carnage.database.repository import item_base_type


def test_item_base_type_repository_init(database_session_mock):
    repository = item_base_type.ItemBaseTypeRepository()
    assert repository.session is not None
