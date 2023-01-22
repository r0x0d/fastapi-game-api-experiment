"""Module that represents the Monster repository."""

from carnage.database.models.base import BaseModel
from carnage.database.models.monster import MonsterModel
from carnage.database.repository.base import BaseRepository


class MonsterRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: BaseModel = MonsterModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
