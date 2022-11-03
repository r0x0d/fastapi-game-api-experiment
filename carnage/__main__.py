import argparse
import importlib.metadata
import logging
import platform
import sys

from carnage.cli import seed, serve
from carnage.logger import setup_logger_handler


def create_argument_parser() -> argparse.ArgumentParser:
    """."""
    parser = argparse.ArgumentParser(
        prog="carnage",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Command-line for Carnage.",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        default=argparse.SUPPRESS,
        help="Print installed Carnage version",
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


def print_version() -> None:
    """Prints version information of carnage game and python."""
    carnage_version = importlib.metadata.version("carnage")
    print(f"Carnage Version   :         {carnage_version}")
    print(f"Python Version    :         {platform.python_version()}")
    print(f"Operating System  :         {platform.platform()}")
    print(f"Python Path       :         {sys.executable}")


def main() -> int:
    arg_parser = create_argument_parser()
    cmdline_arguments = arg_parser.parse_args()

    setup_logger_handler(debug=cmdline_arguments.debug)
    logger = logging.getLogger(__name__)
    try:
        if hasattr(cmdline_arguments, "func"):
            cmdline_arguments.func(cmdline_arguments)
        elif hasattr(cmdline_arguments, "version"):
            print_version()
        else:
            # user has not provided a subcommand, let's print the help
            logger.warning("No command specified.")
            arg_parser.print_help()
            return 1
    except Exception as e:
        logger.error(
            "Failed to run CLI command due to an exception.",
        )
        logger.exception("{}: {}", e.__class__.__name__, e)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
