"""Module that represents the Spell School repository."""

from carnage.database.models.spell import SpellSchoolModel
from carnage.database.repository.base import BaseRepository


class SpellSchoolRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[SpellSchoolModel] = SpellSchoolModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
