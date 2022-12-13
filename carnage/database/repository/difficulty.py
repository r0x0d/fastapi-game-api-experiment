from typing import Type

from carnage.database.models.difficulty import DifficultyModel
from carnage.database.repository.base import BaseRepository


class DifficultyRepository(BaseRepository):
    def __init__(self, model: Type[DifficultyModel] = DifficultyModel) -> None:
        super().__init__(model)
