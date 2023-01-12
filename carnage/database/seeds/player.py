from typing import Any

from carnage.database.repository.dungeon import DungeonRepository
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
        repository: type[PlayerRepository] = PlayerRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.dungeon_repository = DungeonRepository()
        self.vocation_repository = VocationRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
        dungeon = self.dungeon_repository.select_first()
        vocation = self.vocation_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "dungeon_id": dungeon[0].id,
                    "vocation_id": vocation[0].id,
                },
            )

        super().seed()
