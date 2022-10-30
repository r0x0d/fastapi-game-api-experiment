from carnage.database.repository.spell import spell_range_type


def test_spell_range_type_repository_init(database_session_mock):
    repository = spell_range_type.SpellRangeTypeRepository()
    assert repository.session is not None
