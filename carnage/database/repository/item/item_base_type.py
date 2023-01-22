"""Module that represents the Item Base Type repository."""

from carnage.database.models.item.item_base_type import ItemBaseTypeModel
from carnage.database.repository.base import BaseRepository


class ItemBaseTypeRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[ItemBaseTypeModel] = ItemBaseTypeModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
