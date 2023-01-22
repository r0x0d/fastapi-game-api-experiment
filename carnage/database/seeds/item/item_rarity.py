"""Module that represents the Item Rarity seeding."""

from carnage.database.repository.item import ItemRarityRepository
from carnage.database.seeds.base import BaseSeed


class ItemRaritySeed(BaseSeed):
    """Class that overrides the base seed methods."""

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
        repository: type[ItemRarityRepository] = ItemRarityRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
