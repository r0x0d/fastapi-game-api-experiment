import argparse
from collections import namedtuple
from unittest import mock

import pytest

from carnage.cli import seed


def test_add_subparser():
    subparsers = mock.Mock()
    parents = mock.Mock()
    seed.add_subparser(subparsers, parents)

    subparsers.add_parser.assert_called_once_with(
        name="seed",
        parents=parents,
        help="Seed the database with pre-defined data.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )


namespace = namedtuple("Namespace", ("all", "name"))


@mock.patch.object(seed, "SeedManager")
@pytest.mark.parametrize(
    ("args_all", "args_name"),
    ((True, None), (False, "test")),
)
def test_run(seed_manager_mock, args_all, args_name):
    args = namespace(args_all, args_name)

    seed.run(args=args)
    assert seed_manager_mock.seed.called_once()


@pytest.mark.parametrize(
    ("args_all", "args_name", "match"),
    (
        (False, None, "At least one of them needs to be used."),
        (
            True,
            "test",
            "Only `--all` or `--name` can be used at the time. Not both.",
        ),
    ),
)
def test_run_assertion_error(args_all, args_name, match):
    args = namespace(args_all, args_name)
    with pytest.raises(
        AssertionError,
        match=match,
    ):
        seed.run(args=args)
