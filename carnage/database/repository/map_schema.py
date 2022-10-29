from typing import Type

from carnage.database.models.map_schema import MapSchemaModel
from carnage.database.repository.base import BaseRepository


class MapSchemaRepository(BaseRepository):
    def __init__(self, model: Type[MapSchemaModel] = MapSchemaModel) -> None:
        super().__init__(model)
