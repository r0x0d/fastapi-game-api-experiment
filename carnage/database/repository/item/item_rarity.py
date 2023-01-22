"""Module that represents the Item Rarity repository."""

from carnage.database.models.item.item_rarity import ItemRarityModel
from carnage.database.repository.base import BaseRepository


class ItemRarityRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: type[ItemRarityModel] = ItemRarityModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
