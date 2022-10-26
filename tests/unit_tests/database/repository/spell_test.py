from carnage.database.repository import spell


def test_spell_repository_init(database_session_mock):
    repository = spell.SpellRepository()
    assert repository.session is not None
