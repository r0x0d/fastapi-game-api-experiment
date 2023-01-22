"""Module that represents the Monster Type repository."""

from carnage.database.models.base import BaseModel
from carnage.database.models.monster import MonsterTypeModel
from carnage.database.repository.base import BaseRepository


class MonsterTypeRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: BaseModel = MonsterTypeModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
