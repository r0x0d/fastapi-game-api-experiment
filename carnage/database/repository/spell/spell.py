from typing import Type

from carnage.database.models.spell import SpellModel
from carnage.database.repository.base import BaseRepository


class SpellRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SpellModel] = SpellModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
