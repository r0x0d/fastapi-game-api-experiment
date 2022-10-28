import argparse
import logging

import alembic.config

from carnage.cli import SubparserType

logger = logging.getLogger(__name__)


def add_subparser(
    subparsers: SubparserType,
    parents: list[argparse.ArgumentParser],
) -> None:
    """Add all init parsers.
    Args:
        subparsers: subparser we are going to attach to
        parents: Parent parsers, needed to ensure tree structure in argparse
    """
    serve_parser = subparsers.add_parser(
        name="migration",
        parents=parents,
        help="Run carnage migrations.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    serve_parser.set_defaults(func=run)


def run(args: argparse.Namespace) -> None:
    """."""
    logger.info("Running carnage migration")
    alembicArgs = [
        "--raiseerr",
        "upgrade",
        "head",
    ]
    alembic.config.main(argv=alembicArgs)

    logger.info("Migration executed successfully.")
