from carnage.database.repository.spell import spell_school


def test_spell_school_repository_init(database_session_mock):
    repository = spell_school.SpellSchoolRepository()
    assert repository.session is not None
