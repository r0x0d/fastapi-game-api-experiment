import argparse
import importlib.metadata
import platform
import sys

from carnage.cli import seed, serve


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

    try:
        if hasattr(cmdline_arguments, "func"):
            cmdline_arguments.func(cmdline_arguments)
        elif hasattr(cmdline_arguments, "version"):
            print_version()
        else:
            # user has not provided a subcommand, let's print the help
            print("No command specified.")
            arg_parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(
            "Failed to run CLI command due to an exception.",
        )
        print(f"{e.__class__.__name__}: {e}")
        sys.exit(1)

    return 0


if __name__ == "__main__":
    main()
