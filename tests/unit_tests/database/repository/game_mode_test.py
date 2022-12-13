from carnage.database.repository import game_mode


def test_game_mode_repository_init(database_session_mock):
    repository = game_mode.GameModeRepository()
    assert repository.session is not None
