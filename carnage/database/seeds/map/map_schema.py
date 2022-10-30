from typing import Any, Type

from carnage.database.repository.map import (
    MapDifficultyRepository,
    MapSchemaRepository,
)
from carnage.database.seeds.base import BaseSeed


class MapSchemaSeed(BaseSeed):
    name: str = "map_schema"
    data: list[dict[str, Any]] = [
        {"name": "Test schema", "description": "", "schema": {}},
    ]

    def __init__(
        self,
        repository: Type[MapSchemaRepository] = MapSchemaRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.map_difficulty_repository = MapDifficultyRepository()

    def seed(self) -> None:
        map_difficulty = self.map_difficulty_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "map_difficulty_id": map_difficulty[0].id,
                },
            )

        super().seed()
