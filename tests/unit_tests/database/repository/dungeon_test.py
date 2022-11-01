from carnage.database.repository.dungeon import dungeon


def test_dungeon_repository_init(database_session_mock):
    repository = dungeon.DungeonRepository()
    assert repository.session is not None
