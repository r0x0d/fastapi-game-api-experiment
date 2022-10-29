from typing import Type

from carnage.database.models.map import MapModel
from carnage.database.repository.base import BaseRepository


class MapRepository(BaseRepository):
    def __init__(self, model: Type[MapModel] = MapModel) -> None:
        super().__init__(model)
