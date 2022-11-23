from carnage.database.repository.vocation import vocation_spell


def test_vocation_spell_repository_init(database_session_mock):
    repository = vocation_spell.VocationSpellRepository()
    assert repository.session is not None


def test_select_by_spell_id(database_session_mock):
    repository = vocation_spell.VocationSpellRepository()
    repository.select_by_spell_id(spell_id="test")
    assert repository.session is not None
