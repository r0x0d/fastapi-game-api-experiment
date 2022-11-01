from typing import Type

from carnage.database.models.dungeon import DungeonModel
from carnage.database.repository.base import BaseRepository


class DungeonRepository(BaseRepository):
    def __init__(self, model: Type[DungeonModel] = DungeonModel) -> None:
        super().__init__(model)
