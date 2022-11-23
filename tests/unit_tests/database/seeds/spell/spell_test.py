from carnage.database.seeds import spell


def test_spell_seed_init(database_session_mock):
    seed = spell.SpellSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = spell.SpellSeed()
    seed.seed()

    for data in seed.data:
        assert "spell_school_id" in data
        assert "spell_duration_type_id" in data
        assert "spell_range_type_id" in data
