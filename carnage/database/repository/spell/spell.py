"""Module that represents the Spell repository."""

from carnage.database.models.spell import SpellModel
from carnage.database.repository.base import BaseRepository


class SpellRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[SpellModel] = SpellModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
