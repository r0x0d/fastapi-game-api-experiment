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
        repository: type[ItemBaseTypeRepository] = ItemBaseTypeRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
