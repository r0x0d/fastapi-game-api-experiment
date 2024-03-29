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
"""Module that represents the Account seeding."""
import logging
from typing import Any

from cryptography.fernet import Fernet

from carnage.database.models.account import ProviderEnum
from carnage.database.repository.account import AccountRepository
from carnage.database.seeds.base import BaseSeed

logger = logging.getLogger(__name__)


class AccountSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "account"
    data: list[dict[str, str | Any]] = [
        {
            "username": "rodolfo.olivieri3@gmail.com",
            "nickname": "r0x0d",
            "provider": ProviderEnum.google,
            "secret_key": Fernet.generate_key().decode(),
        },
    ]

    def validate_seed(self, seed: dict[str, str]) -> bool:
        """Validate if a seed already exists in the database.

        :param seed: The current seed being seeded.
        """
        logger.debug(
            "Validating the current seed with username: '%s'",
            seed["username"],
        )

        result = self.repository.select_by_username(  # type: ignore
            username=seed["username"],
        )
        if result:
            logger.debug("Seed already exists in the database")
            return True

        return False

    def __init__(
        self,
        repository: type[AccountRepository] = AccountRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
