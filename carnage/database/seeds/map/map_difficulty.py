import logging
from typing import Type

from carnage.database.repository.map import MapDifficultyRepository
from carnage.database.seeds.base import BaseSeed

logger = logging.getLogger(__name__)


class MapDifficultySeed(BaseSeed):
    name: str = "map_difficulty"
    data: list[dict[str, str]] = [
        {
            "level": "Easy",
            "description": "",
        },
        {
            "level": "Medium",
            "description": "",
        },
        {"level": "Hard", "description": ""},
        {"level": "Impossible", "description": ""},
        {"level": "Nightmare", "description": ""},
    ]

    def validate_seed(self, seed: dict[str, str]) -> bool:
        logger.debug(
            "Validating the current seed with level: '%s'",
            seed["level"],
        )

        result = self.repository.select_by_level(  # type: ignore
            level=seed["level"],
        )
        if result:
            logger.debug("Seed already exists in the database")
            return True

        return False

    def __init__(
        self,
        repository: Type[MapDifficultyRepository] = MapDifficultyRepository,
    ) -> None:
        super().__init__(repository=repository)
