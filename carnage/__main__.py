import argparse
import logging
import sys

from carnage.cli import seed, serve
from carnage.logger import setup_logger_handler


def create_argument_parser() -> argparse.ArgumentParser:
    """Create the base argument parser for carnage CLI."""
    parser = argparse.ArgumentParser(
        prog="carnage",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Command-line for Carnage.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Enable debug logging",
    )

    parent_parsers = [argparse.ArgumentParser(add_help=False)]
    subparsers = parser.add_subparsers(help="Carnage sub-commands")

    seed.add_subparser(subparsers, parents=parent_parsers)
    serve.add_subparser(subparsers, parents=parent_parsers)

    return parser


def main() -> int:
    """Main entrypoint for Carnage API."""
    arg_parser = create_argument_parser()
    cmdline_arguments = arg_parser.parse_args()

    setup_logger_handler(debug=cmdline_arguments.debug)
    logger = logging.getLogger(__name__)
    try:
        if hasattr(cmdline_arguments, "func"):
            cmdline_arguments.func(cmdline_arguments)
        else:
            # user has not provided a subcommand, let's print the help
            logger.warning("No command specified.")
            arg_parser.print_help()
            return 1
    except Exception as e:
        logger.error(
            "Failed to run CLI command due to an exception.",
        )
        logger.exception("%s", e)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
