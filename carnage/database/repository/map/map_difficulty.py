from typing import Type

from sqlalchemy import select

from carnage.database.models.map.map_difficulty import MapDifficultyModel
from carnage.database.repository.base import BaseRepository


class MapDifficultyRepository(BaseRepository):
    def __init__(
        self,
        model: Type[MapDifficultyModel] = MapDifficultyModel,
    ) -> None:
        super().__init__(model)

    def select_by_level(self, level: str) -> MapDifficultyModel:
        statement = select(self.model).where(self.model.level == level)

        with self.session() as session:
            return session.execute(statement=statement).first()
