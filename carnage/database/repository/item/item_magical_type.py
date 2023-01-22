"""Module that represents the Item Magical Type repository."""

from carnage.database.models.item import ItemMagicalTypeModel
from carnage.database.repository.base import BaseRepository


class ItemMagicalTypeRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[ItemMagicalTypeModel] = ItemMagicalTypeModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
