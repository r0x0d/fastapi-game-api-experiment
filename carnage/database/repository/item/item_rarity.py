from typing import Type

from carnage.database.models.item.item_rarity import ItemRarityModel
from carnage.database.repository.base import BaseRepository


class ItemRarityRepository(BaseRepository):
    def __init__(self, model: Type[ItemRarityModel] = ItemRarityModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
