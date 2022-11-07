from functools import lru_cache
from typing import Type

from sqlalchemy import select

from carnage.database.models.dungeon import DungeonSchemaModel
from carnage.database.repository.base import BaseRepository


class DungeonSchemaRepository(BaseRepository):
    def __init__(
        self,
        model: Type[DungeonSchemaModel] = DungeonSchemaModel,
    ) -> None:
        super().__init__(model)

    @lru_cache
    def select_by_dungeon_difficulty(
        self,
        dungeon_difficulty_id: str,
    ) -> list[DungeonSchemaModel]:
        statement = select(self.model).where(
            self.model.dungeon_difficulty_id == dungeon_difficulty_id,
        )

        with self.session() as session:
            return session.execute(statement=statement).scalars().all()
