"""Module that represents the Item repository."""

from carnage.database.models.item import ItemModel
from carnage.database.repository.base import BaseRepository


class ItemRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: type[ItemModel] = ItemModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
