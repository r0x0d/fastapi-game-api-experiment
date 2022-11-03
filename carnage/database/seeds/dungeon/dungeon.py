from typing import Any, Type

from carnage.database.repository.dungeon import (
    DungeonDifficultyRepository,
    DungeonRepository,
    DungeonSchemaRepository,
)
from carnage.database.seeds.base import BaseSeed
from carnage.systems.dungeon_generation import generate_dungeon


class DungeonSeed(BaseSeed):
    name: str = "dungeon"
    data: list[dict[str, Any]] = [
        {
            "_dungeon_difficulty": "Easy",
            "name": "Easy dungeon",
            "description": "Easy dungeon",
        },
    ]

    def __init__(
        self,
        repository: Type[DungeonRepository] = DungeonRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.dungeon_schema_repository = DungeonSchemaRepository()
        self.dungeon_difficulty_repository = DungeonDifficultyRepository()

    def seed(self) -> None:

        for item in self.data:
            dungeon_difficulty = (
                self.dungeon_difficulty_repository.select_by_level(
                    level=item["_dungeon_difficulty"],
                )
            )
            dungeon_schema = (
                self.dungeon_schema_repository.select_by_dungeon_difficulty(
                    dungeon_difficulty[0].id,
                )
            )
            plot = generate_dungeon(dungeon_difficulty[0].id)
            item.pop("_dungeon_difficulty")
            item.update(
                {"dungeon_schema_id": dungeon_schema[0].id, "plot": plot},
            )

        super().seed()
