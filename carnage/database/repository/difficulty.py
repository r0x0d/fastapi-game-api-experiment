from typing import Type

from carnage.database.models.difficulty import DifficultyModel
from carnage.database.repository.base import BaseRepository


class DifficultyRepository(BaseRepository):
    def __init__(self, model: Type[DifficultyModel] = DifficultyModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
