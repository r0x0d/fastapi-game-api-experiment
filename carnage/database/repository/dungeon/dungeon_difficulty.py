from functools import lru_cache
from typing import Type

from sqlalchemy import select

from carnage.database.models.dungeon.dungeon_difficulty import (
    DungeonDifficultyModel,
)
from carnage.database.repository.base import BaseRepository


class DungeonDifficultyRepository(BaseRepository):
    def __init__(
        self,
        model: Type[DungeonDifficultyModel] = DungeonDifficultyModel,
    ) -> None:
        super().__init__(model)

    @lru_cache
    def select_by_level(self, level: str) -> DungeonDifficultyModel:
        statement = select(self.model).where(
            self.model.level == level and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()
