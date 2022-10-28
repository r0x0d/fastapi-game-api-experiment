from typing import Type

from carnage.database.models.race import RaceModel
from carnage.database.repository.base import BaseRepository


class RaceRepository(BaseRepository):
    def __init__(self, model: Type[RaceModel] = RaceModel) -> None:
        super().__init__(model)
