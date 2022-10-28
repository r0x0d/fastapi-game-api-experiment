from carnage.database.repository import race


def test_race_repository_init(database_session_mock):
    repository = race.RaceRepository()
    assert repository.session is not None
