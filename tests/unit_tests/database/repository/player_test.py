from carnage.database.repository import player


def test_player_repository_init(database_session_mock):
    repository = player.PlayerRepository()
    assert repository.session is not None
