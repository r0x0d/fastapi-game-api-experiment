from unittest import mock
from unittest.mock import MagicMock

import pytest

from carnage.database.seeds import manager


def test_seed_manager_init(database_session_mock):
    seed = manager.SeedManager()

    assert isinstance(seed, manager.SeedManager)


@pytest.mark.parametrize(
    ("all_seeds", "seed_name"),
    ((False, "test"), (True, None)),
)
def test_seed(database_session_mock, all_seeds, seed_name):
    seed = manager.SeedManager()
    with mock.patch.object(
        seed,
        "seed_mapping",
        return_value={"test": MagicMock()},
    ):
        assert seed.seed(all_seeds, seed_name) is None


def test_seed_assertion_error(database_session_mock):
    seed = manager.SeedManager()
    with mock.patch.object(
        seed,
        "seed_mapping",
        return_value={"test": MagicMock()},
    ):
        with pytest.raises(
            AssertionError,
            match="Couldn't find the desired seed.",
        ):
            seed.seed(all_seeds=False, seed_name="non-existing")


def test_seed_mapping(database_session_mock):
    seed = manager.SeedManager()
    result = seed.seed_mapping()
    assert isinstance(result, dict)
