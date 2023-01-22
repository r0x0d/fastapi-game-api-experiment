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
"""Module that represents the Base seeding."""

import logging
from typing import Any

from carnage.database.repository.base import BaseRepository

logger = logging.getLogger(__name__)


class BaseSeed:
    """Class that implements the base seed methods."""

    name: str = "base"
    data: list[dict[str, Any]] = [{}]

    def __init__(
        self,
        repository: type[BaseRepository] = BaseRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        self.repository = repository()

    def validate_seed(self, seed: dict[str, str]) -> bool:
        """Validate if a seed already exists in the database.

        :param seed: The current seed being seeded.
        """
        logger.debug(
            "Validating the current seed with name: '%s'",
            seed["name"],
        )

        result = self.repository.select_by_name(name=seed["name"])
        if result:
            logger.debug("Seed already exists in the database")
            return True

        return False

    def seed(self) -> None:
        """Method to seed data into the database."""
        if not self.data:
            raise ValueError(f"No seed data found for {self.name}")

        for seed in self.data:
            if not self.validate_seed(seed=seed):
                self.repository.insert(self.data)
                logger.info("Seeded '%s' successfully", self.name)
