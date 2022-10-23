from unittest import mock

import pytest

from carnage.database.seeds import base


def test_monster_seed_init(database_session_mock):
    seed = base.BaseSeed()

    assert seed.name is not None
    assert seed.data is not None


def test_seed(database_session_mock, capsys):
    seed = base.BaseSeed(mock.Mock())
    seed.seed()

    assert "Seeded base" in capsys.readouterr().out


def test_seed_value_error():
    seed = base.BaseSeed(mock.Mock())
    seed.data = None
    with pytest.raises(ValueError, match="No seed data found for base"):
        seed.seed()
