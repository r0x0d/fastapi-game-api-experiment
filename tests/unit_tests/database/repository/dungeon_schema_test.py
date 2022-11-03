from carnage.database.repository.dungeon import dungeon_schema


def test_dungeon_schema_repository_init(database_session_mock):
    repository = dungeon_schema.DungeonSchemaRepository()
    assert repository.session is not None


def test_select_by_dungeon_difficulty(database_session_mock):
    repository = dungeon_schema.DungeonSchemaRepository()
    repository.select_by_dungeon_difficulty(dungeon_difficulty_id="1")
    assert repository.session is not None
