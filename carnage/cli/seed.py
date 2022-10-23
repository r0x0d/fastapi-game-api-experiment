import argparse

from carnage.cli import SubparserType
from carnage.database.seeds.manager import SeedManager


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

    seed_parser.set_defaults(func=run)


def run(args: argparse.Namespace) -> None:
    seed_manager = SeedManager()

    if args.all and args.name:
        raise AssertionError(
            "Only `--all` or `--name` can be used at the time. Not both.",
        )

    if not args.all and not args.name:
        raise AssertionError("At least one of them needs to be used.")

    seed_manager.seed(all_seeds=args.all, seed_name=args.name)
