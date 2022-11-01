from carnage.database.repository.dungeon import dungeon_schema


def test_dungeon_schema_repository_init(database_session_mock):
    repository = dungeon_schema.DungeonSchemaRepository()
    assert repository.session is not None
