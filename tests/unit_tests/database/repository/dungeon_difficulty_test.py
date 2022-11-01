from carnage.database.repository.dungeon import dungeon_difficulty


def test_dungeon_difficulty_repository_init(database_session_mock):
    repository = dungeon_difficulty.DungeonDifficultyRepository()
    assert repository.session is not None


def test_select_by_level(database_session_mock):
    repository = dungeon_difficulty.DungeonDifficultyRepository()
    repository.select_by_level(level="test")
    assert repository.session is not None
