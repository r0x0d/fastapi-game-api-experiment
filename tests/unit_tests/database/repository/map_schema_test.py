from carnage.database.repository.map import map_schema


def test_map_schema_repository_init(database_session_mock):
    repository = map_schema.MapSchemaRepository()
    assert repository.session is not None
