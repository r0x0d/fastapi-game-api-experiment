from typing import Any, Type

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
        },
    ]

    def __init__(
        self,
        repository: Type[VocationRepository] = VocationRepository,
    ) -> None:
        super().__init__(repository=repository)
