import pytest

from carnage.vocations import manager
from carnage.vocations.knight import Knight


def test_vocation_manager_can_initialize():
    vocation_manager = manager.VocationManager()

    assert isinstance(vocation_manager, manager.VocationManager)


def test_vocation_mapping():
    vocation_manager = manager.VocationManager()
    assert isinstance(vocation_manager._vocation_mapping, dict)


@pytest.mark.parametrize(
    ("vocation", "expected"),
    (
        ("non-existing", None),
        ("knight", Knight),
    ),
)
def test_select(vocation, expected):
    vocation_manager = manager.VocationManager()

    result = vocation_manager.select(vocation)
    assert result == expected
