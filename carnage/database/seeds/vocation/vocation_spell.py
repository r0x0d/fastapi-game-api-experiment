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
"""Module that represents the Vocation Spell seeding."""

import logging
from typing import Any

from carnage.database.repository.spell import SpellRepository
from carnage.database.repository.vocation import (
    VocationRepository,
    VocationSpellRepository,
)
from carnage.database.seeds.base import BaseSeed

logger = logging.getLogger(__name__)


class VocationSpellSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "vocation_spell"
    data: list[dict[str, Any]] = [
        {
            "spell_order": 1,
        },
    ]

    def __init__(
        self,
        repository: type[VocationSpellRepository] = VocationSpellRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.vocation_repository = VocationRepository()
        self.spell_repository = SpellRepository()

    def validate_seed(self, seed: dict[str, str]) -> bool:
        """Validate if a seed already exists in the database.

        :param seed: The current seed being seeded.
        """
        logger.debug(
            "Validating the current seed with spell_id: '%s'",
            seed["spell_id"],
        )

        result = self.repository.select_by_spell_id(  # type: ignore
            spell_id=seed["spell_id"],
        )
        if result:
            logger.debug("Seed already exists in the database")
            return True

        return False

    def seed(self) -> None:
        """Method to seed data into the database."""
        vocation = self.vocation_repository.select_first()
        spell = self.spell_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "vocation_id": vocation[0].id,
                    "spell_id": spell[0].id,
                },
            )

        super().seed()
