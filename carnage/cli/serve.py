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
"""Module that represents the `serve` command."""

import argparse
import logging
from typing import Any

import uvicorn

from carnage.application import create_app

logger = logging.getLogger(__name__)


def add_subparser(
    subparsers: Any,
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
