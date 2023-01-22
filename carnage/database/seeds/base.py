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
