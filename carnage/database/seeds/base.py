import logging
from typing import Any, Type

from carnage.database.repository.base import BaseRepository

logger = logging.getLogger(__name__)


class BaseSeed:
    name: str = "base"
    data: list[dict[str, Any]] = [{}]

    def __init__(
        self,
        repository: Type[BaseRepository] = BaseRepository,
    ) -> None:
        self.repository = repository()

    def validate_seed(self, seed: dict[str, str]) -> bool:
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
        if not self.data:
            raise ValueError(f"No seed data found for {self.name}")

        for seed in self.data:
            if not self.validate_seed(seed=seed):
                self.repository.insert(self.data)
                logger.info("Seeded '%s' successfully", self.name)
