from unittest import mock

import pytest

from carnage.database.seeds.dungeon import dungeon_difficulty


def test_dungeon_difficulty_seed_init(database_session_mock):
    seed = dungeon_difficulty.DungeonDifficultySeed()

    assert seed.name is not None
    assert seed.data is not None


@pytest.mark.parametrize(
    ("seed_exist"),
    (
        (True),
        (False),
    ),
)
def test_validate_seed(seed_exist, database_session_mock):
    seed = dungeon_difficulty.DungeonDifficultySeed()
    with mock.patch.object(
        seed.repository,
        "select_by_level",
        lambda level: seed_exist,
    ):
        # We don't care too much about the rest
        assert seed.validate_seed(seed={"level": "test"}) == seed_exist
