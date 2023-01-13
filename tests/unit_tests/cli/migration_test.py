import argparse
from collections import namedtuple
from unittest import mock

import pytest
from alembic.config import Config

from carnage.cli import migration


def test_add_subparser():
    subparsers = mock.Mock()
    parents = mock.Mock()
    migration.add_subparser(subparsers, parents)

    subparsers.add_parser.assert_called_once_with(
        name="migration",
        parents=parents,
        help="Execute the database migration with Alembic.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )


namespace = namedtuple("Namespace", ("downgrade", "upgrade"))


@mock.patch.object(migration, "command")
@pytest.mark.parametrize(
    ("downgrade", "upgrade"),
    ((True, None), (False, True)),
)
def test_run(command_mock, downgrade, upgrade):
    args = namespace(downgrade, upgrade)

    migration.run(args=args)

    if downgrade:
        assert command_mock.downgrade.called_once()

    if upgrade:
        assert command_mock.upgrade.called_once()


def test_run_assertion_error():
    args = namespace(True, True)

    with pytest.raises(
        AssertionError,
        match="Can't do a downgrade and upgrade at the same time. Must "
        "specify one at a time.",
    ):
        migration.run(args=args)


def test_load_alembic_init():
    result = migration._load_alembic_init()
    assert isinstance(result, Config)
