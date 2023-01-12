import logging

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
        {"level": "Nightmare", "description": ""},
    ]

    def validate_seed(self, seed: dict[str, str]) -> bool:
        """Validate if a seed already exists in the database.

        :param seed: The current seed being seeded.
        """
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
        repository: type[
            DungeonDifficultyRepository
        ] = DungeonDifficultyRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
