import logging
from typing import Any, Type

from carnage.database.repository.spell import SpellRepository
from carnage.database.repository.vocation import (
    VocationRepository,
    VocationSpellRepository,
)
from carnage.database.seeds.base import BaseSeed

logger = logging.getLogger(__name__)


class VocationSpellSeed(BaseSeed):
    name: str = "vocation_spell"
    data: list[dict[str, Any]] = [
        {
            "spell_order": 1,
        },
    ]

    def __init__(
        self,
        repository: Type[VocationSpellRepository] = VocationSpellRepository,
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
