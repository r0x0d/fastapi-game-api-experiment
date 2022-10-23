import argparse
from collections import namedtuple
from unittest import mock

from carnage.cli import serve


def test_add_subparser():
    subparsers = mock.Mock()
    parents = mock.Mock()
    serve.add_subparser(subparsers, parents)

    subparsers.add_parser.assert_called_once_with(
        name="serve",
        parents=parents,
        help="Run carnage backend.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )


namespace = namedtuple("Namespace", ("host", "port"))


@mock.patch.object(serve, "uvicorn")
@mock.patch.object(serve, "create_app")
def test_run(uvicorn_mock, create_app_mock):
    args = namespace("127.0.0.1", 5050)

    serve.run(args=args)
    assert uvicorn_mock.Config.called_once()
    assert uvicorn_mock.Server.called_once()
