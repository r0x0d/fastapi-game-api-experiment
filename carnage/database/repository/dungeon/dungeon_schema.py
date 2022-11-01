from typing import Type

from carnage.database.models.dungeon.dungeon_schema import DungeonSchemaModel
from carnage.database.repository.base import BaseRepository


class DungeonSchemaRepository(BaseRepository):
    def __init__(
        self,
        model: Type[DungeonSchemaModel] = DungeonSchemaModel,
    ) -> None:
        super().__init__(model)
