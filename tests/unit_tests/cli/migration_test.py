import argparse
import logging
from unittest import mock

from carnage.cli import migration


def test_add_subparser():
    subparsers = mock.Mock()
    parents = mock.Mock()
    migration.add_subparser(subparsers, parents)

    subparsers.add_parser.assert_called_once_with(
        name="migration",
        parents=parents,
        help="Run carnage migrations.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )


@mock.patch.object(migration.alembic.config, "main")
def test_run(alembic_mock, caplog):
    caplog.set_level(logging.INFO)
    migration.run(args=None)

    assert "Migration executed successfully." in caplog.records[-1].message
