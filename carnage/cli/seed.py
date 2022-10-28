import argparse
import logging

from rich.console import Console
from rich.table import Table

from carnage.cli import SubparserType
from carnage.database.seeds.manager import SeedManager

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
    seed_parser = subparsers.add_parser(
        name="seed",
        parents=parents,
        help="Seed the database with pre-defined data.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    seed_parser.add_argument(
        "--all",
        action="store_true",
        help="Run all seeds in the database",
    )
    seed_parser.add_argument(
        "--name",
        default=None,
        help="Name of a specific seed to run.",
    )
    seed_parser.add_argument(
        "--list-seeds",
        action="store_true",
        default=False,
        help="List all seeds",
    )

    seed_parser.set_defaults(func=run)


def _print_seeds_table(manager: SeedManager) -> None:
    table = Table(title="Available Seeds")

    table.add_column("Name", justify="left", style="cyan", no_wrap=False)

    for name, _ in manager.seed_mapping.items():
        table.add_row(name)

    console = Console()
    console.print(table)


def run(args: argparse.Namespace) -> None:
    manager = SeedManager()

    if args.list_seeds:
        _print_seeds_table(manager)
        return

    if args.all and args.name:
        raise AssertionError(
            "Only `--all` or `--name` can be used at the time. Not both.",
        )

    if not args.all and not args.name:
        raise AssertionError("At least one of them needs to be used.")

    name = args.name if args.name else "all"
    logger.debug("Logging seed '%s'", name)
    manager.seed(all_seeds=args.all, seed_name=args.name)
