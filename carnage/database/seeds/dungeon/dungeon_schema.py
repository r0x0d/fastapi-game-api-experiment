from typing import Any, Type

from carnage.database.repository.dungeon import (
    DungeonDifficultyRepository,
    DungeonSchemaRepository,
)
from carnage.database.seeds.base import BaseSeed


class DungeonSchemaSeed(BaseSeed):
    name: str = "dungeon_schema"
    data: list[dict[str, Any]] = [
        {"name": "Test schema", "description": "", "schema": {}},
    ]

    def __init__(
        self,
        repository: Type[DungeonSchemaRepository] = DungeonSchemaRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.dungeon_difficulty_repository = DungeonDifficultyRepository()

    def seed(self) -> None:
        dungeon_difficulty = self.dungeon_difficulty_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "dungeon_difficulty_id": dungeon_difficulty[0].id,
                },
            )

        super().seed()
