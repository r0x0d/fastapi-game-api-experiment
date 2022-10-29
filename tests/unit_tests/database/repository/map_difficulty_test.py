from carnage.database.repository import map_difficulty


def test_map_difficulty_repository_init(database_session_mock):
    repository = map_difficulty.MapDifficultyRepository()
    assert repository.session is not None


def test_select_by_level(database_session_mock):
    repository = map_difficulty.MapDifficultyRepository()
    repository.select_by_level(level="test")
    assert repository.session is not None
