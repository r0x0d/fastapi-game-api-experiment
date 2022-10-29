from typing import Any, Type

from carnage.database.repository.map import MapRepository
from carnage.database.repository.player import PlayerRepository
from carnage.database.repository.vocation import VocationRepository
from carnage.database.seeds.base import BaseSeed


class PlayerSeed(BaseSeed):
    name: str = "player"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
            "is_alive": True,
        },
    ]

    def __init__(
        self,
        repository: Type[PlayerRepository] = PlayerRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.map_repository = MapRepository()
        self.vocation_repository = VocationRepository()

    def seed(self) -> None:
        map = self.map_repository.select_first()
        vocation = self.vocation_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "map_id": map[0].id,
                    "vocation_id": vocation[0].id,
                },
            )

        super().seed()
