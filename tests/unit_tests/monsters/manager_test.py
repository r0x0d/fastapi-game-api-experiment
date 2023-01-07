import pytest

from carnage.monsters import manager
from carnage.monsters.dragon import Dragon


def test_monster_manager_can_initialize():
    monster_manager = manager.MonsterManager()

    assert isinstance(monster_manager, manager.MonsterManager)


def test_monster_mapping():
    monster_manager = manager.MonsterManager()
    assert isinstance(monster_manager._monster_mapping, dict)


@pytest.mark.parametrize(
    ("monster", "expected"),
    (
        ("non-existing", None),
        ("dragon", Dragon),
    ),
)
def test_select(monster, expected):
    monster_manager = manager.MonsterManager()

    result = monster_manager.select(monster)
    assert result == expected
