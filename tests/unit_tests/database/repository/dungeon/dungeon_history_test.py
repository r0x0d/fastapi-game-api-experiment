from carnage.database.repository.dungeon import dungeon_history


def test_dungeon_history_repository_init(database_session_mock):
    repository = dungeon_history.DungeonHistoryRepository()
    assert repository.session is not None


def test_select_by_player_id(database_session_mock):
    repository = dungeon_history.DungeonHistoryRepository()
    repository.select_by_player_id(player_id="test")
    assert repository.session is not None


def test_select_by_dungeon_id(database_session_mock):
    repository = dungeon_history.DungeonHistoryRepository()
    repository.select_by_dungeon_id(dungeon_id="test")
    assert repository.session is not None


def test_select_by_player_and_dungeon_id(database_session_mock):
    repository = dungeon_history.DungeonHistoryRepository()
    repository.select_by_player_and_dungeon_id(
        player_id="test",
        dungeon_id="test",
    )
    assert repository.session is not None
