import pytest

from carnage.database.models.spell import SpellModel
from carnage.spells.fireball import Fireball


def test_spell_can_initialize():
    spell = Fireball(SpellModel())
    assert spell.spell is not None
    assert isinstance(spell, Fireball)


@pytest.mark.parametrize(
    (
        "damage_type",
        "base_damage",
        "attribute_modifier",
        "player_defense",
        "expected_damage",
    ),
    (
        (1, 10, 2, 5, 19),  # Normal hit
        (2, 2, 2, 5, 7),  # Critical hit
        (1, 2, 9, 2, 17),
        (2, 2, 9, 2, 35),
    ),
)
def test_spell_attack(
    damage_type,
    base_damage,
    attribute_modifier,
    player_defense,
    expected_damage,
):
    model = SpellModel()
    model.base_damage = base_damage
    spell = Fireball(model)

    damage = spell.attack(damage_type, attribute_modifier, player_defense)
    assert damage == expected_damage


@pytest.mark.parametrize(
    (
        "damage_type",
        "base_magical_damage",
        "attribute_modifier",
        "player_magical_defense",
        "expected_damage",
    ),
    (
        (1, 10, 3, 15, 12),
        (2, 10, 5, 5, 66),
        (1, 10, 2, 5, 13),
        (1, 20, 9, 10, 120),
        (1, 20, 10, 3, 173),
        (2, 20, 4, 3, 139),
    ),
)
def test_spell_magical_attack(
    damage_type,
    base_magical_damage,
    attribute_modifier,
    player_magical_defense,
    expected_damage,
):
    model = SpellModel()
    model.base_magical_damage = base_magical_damage
    spell = Fireball(model)

    damage = spell.magical_attack(
        damage_type,
        attribute_modifier,
        player_magical_defense,
    )
    assert damage == expected_damage


def test_spell_can_perform_attack():
    # TODO(r0x0d): Improve this test in the future when we have a good system
    # for hit chance.
    model = SpellModel()
    model.attack_threshold = 10
    spell = Fireball(model)

    can_attack = spell.can_perform_attack()

    assert can_attack is not None


def test_spell_can_perform_critical_attack():
    model = SpellModel()
    model.critical_attack_threshold = 10
    spell = Fireball(model)

    can_critically_attack = spell.can_perform_critical_attack()
    assert can_critically_attack is not None
