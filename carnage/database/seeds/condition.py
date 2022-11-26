from typing import Type

from carnage.database.repository.condition import ConditionRepository
from carnage.database.seeds.base import BaseSeed


class ConditionSeed(BaseSeed):
    name: str = "condition"
    data: list[dict[str, str | bool]] = [
        {
            "name": "Blind",
            "description": "Apply blind.",
            "is_permanent": False,
        },
        {
            "name": "Permanent Slow",
            "description": "Apply a permanent slow",
            "is_permanent": True,
        },
    ]

    def __init__(
        self,
        repository: Type[ConditionRepository] = ConditionRepository,
    ) -> None:
        super().__init__(repository=repository)
