"""Module that represents the Monster seeding."""

from typing import Any

from carnage.database.repository.aligment import AligmentRepository
from carnage.database.repository.monster import (
    MonsterRepository,
    MonsterTypeRepository,
)
from carnage.database.repository.size import SizeRepository
from carnage.database.seeds.base import BaseSeed


class MonsterSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "monster"
    data: list[dict[str, Any]] = [
        {
            "name": "Dragon",
            "description": "A mighty dragon.",
            "hitpoints": 200,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
            "is_boss": False,
            "attack_threshold": 90,
            "critical_attack_threshold": 50,
        },
        {
            "name": "Test2",
            "description": "Test description",
            "hitpoints": 200,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
            "is_boss": False,
            "attack_threshold": 90,
            "critical_attack_threshold": 50,
        },
        {
            "name": "Test3",
            "description": "Test description",
            "hitpoints": 200,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
            "is_boss": False,
            "attack_threshold": 90,
            "critical_attack_threshold": 50,
        },
        {
            "name": "Test4",
            "description": "Test description",
            "hitpoints": 200,
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
            "is_boss": True,
            "attack_threshold": 90,
            "critical_attack_threshold": 50,
        },
    ]

    def __init__(
        self,
        repository: type[MonsterRepository] = MonsterRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.size_repository = SizeRepository()
        self.monster_type_repository = MonsterTypeRepository()
        self.aligment_repository = AligmentRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
        aligment = self.aligment_repository.select_first()
        size = self.size_repository.select_first()
        monster_type = self.monster_type_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "aligment_id": aligment[0].id,
                    "size_id": size[0].id,
                    "monster_type_id": monster_type[0].id,
                },
            )

        super().seed()
