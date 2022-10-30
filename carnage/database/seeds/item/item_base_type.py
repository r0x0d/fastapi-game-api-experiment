from typing import Type

from carnage.database.repository.item import ItemBaseTypeRepository
from carnage.database.seeds.base import BaseSeed


class ItemBaseTypeSeed(BaseSeed):
    name: str = "item-base-type"
    data: list[dict[str, str]] = [
        {
            "name": "Item",
            "description": "",
        },
        {
            "name": "Armor",
            "description": "",
        },
        {"name": "Weapon", "description": ""},
    ]

    def __init__(
        self,
        repository: Type[ItemBaseTypeRepository] = ItemBaseTypeRepository,
    ) -> None:
        super().__init__(repository=repository)
