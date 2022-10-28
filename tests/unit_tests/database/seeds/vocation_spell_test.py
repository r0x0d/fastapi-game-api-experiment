from unittest import mock

import pytest

from carnage.database.seeds import vocation_spell


def test_vocation_spell_seed_init(database_session_mock):
    seed = vocation_spell.VocationSpellSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock):
    seed = vocation_spell.VocationSpellSeed()
    seed.seed()

    for data in seed.data:
        assert "vocation_id" in data
        assert "spell_id" in data


@pytest.mark.parametrize(
    ("seed_exist"),
    (
        (True),
        (False),
    ),
)
def test_validate_seed(seed_exist, database_session_mock):
    seed = vocation_spell.VocationSpellSeed()
    with mock.patch.object(
        seed.repository,
        "select_by_spell_id",
        lambda spell_id: seed_exist,
    ):
        # We don't care too much about the rest
        assert (
            seed.validate_seed(
                seed={"spell_id": "791cf7d2-5664-11ed-b136-641c67e34d72"},
            )
            == seed_exist
        )
