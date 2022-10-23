from carnage.database.seeds import manager
import pytest


def test_seed_manager_init(database_session_mock):
    seed = manager.SeedManager()

    assert isinstance(seed, manager.SeedManager)


@pytest.mark.parametrize(
    ("all_seeds", "seed_name"), ((False, "monster"), (True, None))
)
def test_seed(database_session_mock, all_seeds, seed_name):
    seed = manager.SeedManager()

    assert seed.seed(all_seeds, seed_name) is None
