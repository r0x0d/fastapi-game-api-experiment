from carnage.database.seeds.spell import spell_school


def test_spell_school_seed_init(database_session_mock):
    seed = spell_school.SpellSchoolSeed()

    assert seed.name is not None
    assert seed.data is not None
