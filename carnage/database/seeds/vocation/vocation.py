from typing import Any

from carnage.database.repository.vocation import VocationRepository
from carnage.database.seeds.base import BaseSeed


class VocationSeed(BaseSeed):
    name: str = "vocation"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
            "hitpoints": 200,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
            "attack_threshold": 90,
            "critical_attack_threshold": 50,
        },
    ]

    def __init__(
        self,
        repository: type[VocationRepository] = VocationRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
