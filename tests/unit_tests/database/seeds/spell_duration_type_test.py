from carnage.database.seeds import spell_duration_type


def test_spell_duration_type_seed_init(database_session_mock):
    seed = spell_duration_type.SpellDurationTypeSeed()

    assert seed.name is not None
    assert seed.data is not None
