from typing import Any, Type

from carnage.database.repository.monster_type import MonsterTypeRepository
from carnage.database.seeds.base import BaseSeed


class MonsterTypeSeed(BaseSeed):
    name: str = "monster_type"
    data: list[dict[str, Any]] = [
        {
            "name": "Dragon",
        },
        {
            "name": "Kobold",
        },
        {
            "name": "Undead",
        },
    ]

    def __init__(
        self,
        repository: Type[MonsterTypeRepository] = MonsterTypeRepository,
    ) -> None:
        super().__init__(repository=repository)
