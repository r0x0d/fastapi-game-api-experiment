from carnage.database.seeds.spell import spell_range_type


def test_spell_range_type_seed_init(database_session_mock):
    seed = spell_range_type.SpellRangeTypeSeed()

    assert seed.name is not None
    assert seed.data is not None
