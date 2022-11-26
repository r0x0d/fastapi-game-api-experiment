from functools import lru_cache
from typing import Type

from sqlalchemy import select

from carnage.database.models.dungeon.dungeon_history import DungeonHistoryModel
from carnage.database.repository.base import BaseRepository


class DungeonHistoryRepository(BaseRepository):
    def __init__(
        self,
        model: Type[DungeonHistoryModel] = DungeonHistoryModel,
    ) -> None:
        super().__init__(model)

    @lru_cache
    def select_by_player_id(self, player_id: str) -> DungeonHistoryModel:
        statement = select(self.model).where(
            self.model.player_id == player_id
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()

    @lru_cache
    def select_by_dungeon_id(self, dungeon_id: str) -> DungeonHistoryModel:
        statement = select(self.model).where(
            self.model.dungeon_id == dungeon_id
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()

    @lru_cache
    def select_by_player_and_dungeon_id(
        self,
        player_id: str,
        dungeon_id: str,
    ) -> DungeonHistoryModel:
        statement = select(self.model).where(
            self.model.player_id == player_id
            and self.model.dungeon_id == dungeon_id
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()
