from typing import Any, Type

from carnage.database.repository.dungeon import (
    DungeonRepository,
    DungeonSchemaRepository,
)
from carnage.database.seeds.base import BaseSeed


class DungeonSeed(BaseSeed):
    name: str = "dungeon"
    data: list[dict[str, Any]] = [
        {"name": "Test dungeon", "description": "", "plot": {}},
    ]

    def __init__(
        self,
        repository: Type[DungeonRepository] = DungeonRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.dungeon_schema_repository = DungeonSchemaRepository()

    def seed(self) -> None:
        dungeon_schema = self.dungeon_schema_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "dungeon_schema_id": dungeon_schema[0].id,
                },
            )

        super().seed()
