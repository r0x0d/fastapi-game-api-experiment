from carnage.database.repository import difficulty


def test_difficulty_repository_init(database_session_mock):
    repository = difficulty.DifficultyRepository()
    assert repository.session is not None
