import pytest

from carnage.database.models.monster.monster import MonsterModel
from carnage.monsters.dragon import Dragon


def test_monster_can_initialize():
    monster = Dragon(MonsterModel())
    assert monster.monster is not None
    assert isinstance(monster, Dragon)


@pytest.mark.parametrize(
    ("damage", "hitpoints", "hitpoints_expected"),
    ((10, 9, 0), (1, 10, 9), (100, 10, 0), (100, -10, 0)),
)
def test_monster_take_damage(damage, hitpoints, hitpoints_expected):
    model = MonsterModel()
    model.hitpoints = hitpoints
    monster = Dragon(model)
    monster.take_damage(damage)

    assert monster.current_hitpoints == hitpoints_expected


def test_monster_take_damage_twice():
    model = MonsterModel()
    model.hitpoints = 10
    monster = Dragon(model)
    monster.take_damage(9)
    monster.take_damage(2)

    assert monster.current_hitpoints == 0


@pytest.mark.parametrize(
    (
        "damage_type",
        "base_damage",
        "prefered_attribute_value",
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
def test_monster_attack(
    damage_type,
    base_damage,
    prefered_attribute_value,
    player_defense,
    expected_damage,
):
    model = MonsterModel()
    model.base_damage = base_damage
    model.strength = prefered_attribute_value
    monster = Dragon(model)

    damage = monster.attack(damage_type, player_defense)
    assert damage == expected_damage


@pytest.mark.parametrize(
    (
        "damage_type",
        "base_magical_damage",
        "prefered_attribute_value",
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
def test_monster_magical_attack(
    damage_type,
    base_magical_damage,
    prefered_attribute_value,
    player_magical_defense,
    expected_damage,
):
    model = MonsterModel()
    model.base_magical_damage = base_magical_damage
    model.intelligence = prefered_attribute_value
    monster = Dragon(model)

    damage = monster.magical_attack(damage_type, player_magical_defense)
    assert damage == expected_damage


def test_monster_can_perform_attack():
    # TODO(r0x0d): Improve this test in the future when we have a good system
    # for hit chance.
    model = MonsterModel()
    model.attack_threshold = 10
    monster = Dragon(model)

    can_attack = monster.can_perform_attack()

    assert can_attack is not None


def test_monster_can_perform_critical_attack():
    model = MonsterModel()
    model.critical_attack_threshold = 10
    monster = Dragon(model)

    can_critically_attack = monster.can_perform_critical_attack()
    assert can_critically_attack is not None


@pytest.mark.parametrize(
    ("hitpoints", "expected"),
    (
        (100, True),
        (0, False),
        (-1, False),
    ),
)
def test_monster_is_alive(hitpoints, expected):
    model = MonsterModel()
    model.hitpoints = hitpoints
    monster = Dragon(model)

    assert monster.is_alive == expected


def test_monster_prefered_attack_attribute():
    model = MonsterModel()
    model.strength = 10
    monster = Dragon(model)

    assert monster.prefered_attack_attribute == 10
    assert monster.monster.dexterity is None


def test_monster_prefered_magical_attack_attribute():
    model = MonsterModel()
    model.intelligence = 10
    monster = Dragon(model)

    assert monster.prefered_magical_attack_attribute == 10
    assert monster.monster.dexterity is None
