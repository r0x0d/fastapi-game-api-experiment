from carnage.database.repository import condition


def test_condition_repository_init(database_session_mock):
    repository = condition.ConditionRepository()
    assert repository.session is not None
