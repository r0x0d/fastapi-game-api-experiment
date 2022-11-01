import logging
from typing import Type

from carnage.database.repository.dungeon import DungeonDifficultyRepository
from carnage.database.seeds.base import BaseSeed

logger = logging.getLogger(__name__)


class DungeonDifficultySeed(BaseSeed):
    name: str = "dungeon_difficulty"
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
        repository: Type[
            DungeonDifficultyRepository
        ] = DungeonDifficultyRepository,
    ) -> None:
        super().__init__(repository=repository)
