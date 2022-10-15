from typing import Any, Type

from carnage.database.repository.aligment import AligmentRepository
from carnage.database.repository.monster import MonsterRepository
from carnage.database.repository.monster_type import MonsterTypeRepository
from carnage.database.repository.size import SizeRepository
from carnage.database.seeds.base import BaseSeed


class MonsterSeed(BaseSeed):
    name: str = "monster"
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
        repository: Type[MonsterRepository] = MonsterRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.size_repository = SizeRepository()
        self.monster_type_repository = MonsterTypeRepository()
        self.aligment_repository = AligmentRepository()

    def seed(self) -> None:
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
