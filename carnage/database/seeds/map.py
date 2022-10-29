from typing import Any, Type

from carnage.database.repository.map import MapRepository
from carnage.database.repository.map_schema import MapSchemaRepository
from carnage.database.seeds.base import BaseSeed


class MapSeed(BaseSeed):
    name: str = "map"
    data: list[dict[str, Any]] = [
        {"name": "Test map", "description": "", "plot": {}},
    ]

    def __init__(
        self,
        repository: Type[MapRepository] = MapRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.map_schema_repository = MapSchemaRepository()

    def seed(self) -> None:
        map_schema = self.map_schema_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "map_schema_id": map_schema[0].id,
                },
            )

        super().seed()
