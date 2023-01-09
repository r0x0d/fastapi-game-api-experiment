import argparse
import logging

import uvicorn

from carnage.application import create_app
from carnage.cli import SubparserType

logger = logging.getLogger(__name__)


def add_subparser(
    subparsers: SubparserType,
    parents: list[argparse.ArgumentParser],
) -> None:
    """Add all init parsers.

    :param subparsers: subparser we are going to attach to
    :param parents: Parent parsers, needed to ensure tree structure argparse.
    """
    serve_parser = subparsers.add_parser(
        name="serve",
        parents=parents,
        help="Run carnage backend.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    serve_parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host address for carnage server.",
    )
    serve_parser.add_argument(
        "--port",
        default=5050,
        help="Port for carnage server.",
    )

    serve_parser.set_defaults(func=run)


def run(args: argparse.Namespace) -> None:
    """Default method that is executed that is tied to the serve command.

    :param args: Arguments passed down to the command.
    """
    logger.debug(
        "Serving carnage at host '%s' with port '%s'.",
        (args.host, args.port),
    )
    config = uvicorn.Config(
        create_app(),
        host=args.host,
        port=args.port,
        log_level="info",
    )
    server = uvicorn.Server(config)
    server.run()
