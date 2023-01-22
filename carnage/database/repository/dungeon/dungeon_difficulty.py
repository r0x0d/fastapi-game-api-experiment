"""Module that represents the Dungeon Difficulty repository."""

from functools import lru_cache

from sqlalchemy import select

from carnage.database.models.dungeon.dungeon_difficulty import (
    DungeonDifficultyModel,
)
from carnage.database.repository.base import BaseRepository


class DungeonDifficultyRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[DungeonDifficultyModel] = DungeonDifficultyModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)

    @lru_cache
    def select_by_level(self, level: str) -> DungeonDifficultyModel:
        """Get results from database filtering by level.

        :param level: Level to be used in the filter.
        """
        statement = select(self.model).where(
            self.model.level == level and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()
