import pytest

from carnage.database.models.vocation import VocationModel
from carnage.vocations.knight import Knight


def test_vocation_can_initialize():
    vocation = Knight(VocationModel())
    assert vocation.vocation is not None
    assert isinstance(vocation, Knight)


@pytest.mark.parametrize(
    ("damage", "hitpoints", "hitpoints_expected"),
    ((10, 9, 0), (1, 10, 9), (100, 10, 0), (100, -10, 0)),
)
def test_vocation_take_damage(damage, hitpoints, hitpoints_expected):
    model = VocationModel()
    model.hitpoints = hitpoints
    vocation = Knight(model)
    vocation.take_damage(damage)

    assert vocation.current_hitpoints == hitpoints_expected


def test_vocation_take_damage_twice():
    model = VocationModel()
    model.hitpoints = 10
    vocation = Knight(model)
    vocation.take_damage(9)
    vocation.take_damage(2)

    assert vocation.current_hitpoints == 0


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
def test_vocation_attack(
    damage_type,
    base_damage,
    prefered_attribute_value,
    player_defense,
    expected_damage,
):
    model = VocationModel()
    model.base_damage = base_damage
    model.strength = prefered_attribute_value
    vocation = Knight(model)

    damage = vocation.attack(damage_type, player_defense)
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
def test_vocation_magical_attack(
    damage_type,
    base_magical_damage,
    prefered_attribute_value,
    player_magical_defense,
    expected_damage,
):
    model = VocationModel()
    model.base_magical_damage = base_magical_damage
    model.intelligence = prefered_attribute_value
    vocation = Knight(model)

    damage = vocation.magical_attack(damage_type, player_magical_defense)
    assert damage == expected_damage


def test_vocation_can_perform_attack():
    # TODO(r0x0d): Improve this test in the future when we have a good system
    # for hit chance.
    model = VocationModel()
    model.attack_threshold = 10
    vocation = Knight(model)

    can_attack = vocation.can_perform_attack()

    assert can_attack is not None


def test_vocation_can_perform_critical_attack():
    model = VocationModel()
    model.critical_attack_threshold = 10
    vocation = Knight(model)

    can_critically_attack = vocation.can_perform_critical_attack()
    assert can_critically_attack is not None


@pytest.mark.parametrize(
    ("hitpoints", "expected"),
    (
        (100, True),
        (0, False),
        (-1, False),
    ),
)
def test_vocation_is_alive(hitpoints, expected):
    model = VocationModel()
    model.hitpoints = hitpoints
    vocation = Knight(model)

    assert vocation.is_alive == expected


def test_vocation_prefered_attack_attribute():
    model = VocationModel()
    model.strength = 10
    vocation = Knight(model)

    assert vocation.prefered_attack_attribute == 10
    assert vocation.vocation.dexterity is None


def test_vocation_prefered_magical_attack_attribute():
    model = VocationModel()
    model.intelligence = 10
    vocation = Knight(model)

    assert vocation.prefered_magical_attack_attribute == 10
    assert vocation.vocation.dexterity is None
