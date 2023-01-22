"""Module that represents the Spell Duration Type repository."""

from carnage.database.models.spell import SpellDurationTypeModel
from carnage.database.repository.base import BaseRepository


class SpellDurationTypeRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[SpellDurationTypeModel] = SpellDurationTypeModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
