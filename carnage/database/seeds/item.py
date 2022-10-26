from typing import Any, Type

from carnage.database.repository.item import ItemRepository
from carnage.database.repository.item_base_type import ItemBaseTypeRepository
from carnage.database.repository.item_magical_type import (
    ItemMagicalTypeRepository,
)
from carnage.database.repository.item_rarity import ItemRarityRepository
from carnage.database.seeds.base import BaseSeed


class ItemSeed(BaseSeed):
    name: str = "item"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
        },
    ]

    def __init__(
        self,
        repository: Type[ItemRepository] = ItemRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.item_rarity_repository = ItemRarityRepository()
        self.item_base_type_repository = ItemBaseTypeRepository()
        self.item_magical_type_repository = ItemMagicalTypeRepository()

    def seed(self) -> None:
        item_rarity = self.item_rarity_repository.select_first()
        item_base_type = self.item_base_type_repository.select_first()
        item_magical_type = self.item_magical_type_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "item_rarity_id": item_rarity[0].id,
                    "item_base_type_id": item_base_type[0].id,
                    "item_magical_type_id": item_magical_type[0].id,
                },
            )

        super().seed()
