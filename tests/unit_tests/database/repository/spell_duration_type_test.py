from carnage.database.repository import spell_duration_type


def test_spell_duration_type_repository_init(database_session_mock):
    repository = spell_duration_type.SpellDurationTypeRepository()
    assert repository.session is not None
