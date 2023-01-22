"""Module that represents the Difficulty repository."""

from carnage.database.models.difficulty import DifficultyModel
from carnage.database.repository.base import BaseRepository


class DifficultyRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: type[DifficultyModel] = DifficultyModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
