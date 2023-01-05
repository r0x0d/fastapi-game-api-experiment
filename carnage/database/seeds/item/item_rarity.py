from typing import Type

from carnage.database.repository.item import ItemRarityRepository
from carnage.database.seeds.base import BaseSeed


class ItemRaritySeed(BaseSeed):
    name: str = "item-rarity"
    data: list[dict[str, str]] = [
        {
            "name": "Artifact",
            "description": "",
        },
        {
            "name": "Common",
            "description": "",
        },
        {"name": "Legendary", "description": ""},
        {"name": "Rare", "description": ""},
        {"name": "Uncommon", "description": ""},
        {"name": "Unknown Rarity", "description": ""},
        {"name": "Varies", "description": ""},
        {"name": "Very Rare", "description": ""},
    ]

    def __init__(
        self,
        repository: Type[ItemRarityRepository] = ItemRarityRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
