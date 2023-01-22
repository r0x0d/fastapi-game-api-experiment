# MIT License
#
# Copyright (c) 2022, Rodolfo Olivieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Module that represents the `seed` command."""

import argparse
import logging
from typing import Any

from rich.console import Console
from rich.table import Table

from carnage.database.seeds.manager import SeedManager

logger = logging.getLogger(__name__)


def add_subparser(
    subparsers: Any,
    parents: list[argparse.ArgumentParser],
) -> None:
    """Add all init parsers.

    :param subparsers: subparser we are going to attach to
    :param parents: Parent parsers, needed to ensure tree structure argparse.
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
    """Print the seed table available for seeding.

    :param manager: The seed manager class that handles the seed order.
    """
    table = Table(title="Available Seeds")

    table.add_column("Name", justify="left", style="cyan", no_wrap=False)

    for name, _ in manager.seed_mapping().items():
        table.add_row(name)

    console = Console()
    console.print(table)


def run(args: argparse.Namespace) -> None:
    """Default method that is executed that is tied to the seed command.

    :param args: Arguments passed down to the command.
    """
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
