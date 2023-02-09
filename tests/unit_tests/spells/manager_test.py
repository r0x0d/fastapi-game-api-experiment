import pytest

from carnage.spells import manager
from carnage.spells.fireball import Fireball


def test_spell_manager_can_initialize():
    spell_manager = manager.SpellManager()

    assert isinstance(spell_manager, manager.SpellManager)


def test_spell_mapping():
    spell_manager = manager.SpellManager()
    assert isinstance(spell_manager._spell_mapping, dict)


@pytest.mark.parametrize(
    ("spell", "expected"),
    (
        ("non-existing", None),
        ("fireball", Fireball),
    ),
)
def test_select(spell, expected):
    spell_manager = manager.SpellManager()

    result = spell_manager.select(spell)
    assert result == expected
