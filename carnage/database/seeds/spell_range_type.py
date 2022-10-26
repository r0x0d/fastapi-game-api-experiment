from typing import Type

from carnage.database.repository.spell_range_type import (
    SpellRangeTypeRepository,
)
from carnage.database.seeds.base import BaseSeed


class SpellRangeTypeSeed(BaseSeed):
    name: str = "spell-range-type"
    data: list[dict[str, str]] = [
        {
            "name": "Self",
            "description": "Self range",
        },
        {
            "name": "Touch",
            "description": "Touch range",
        },
        {
            "name": "Ranged",
            "description": "Ranged range",
        },
        {
            "name": "Sight",
            "description": "Sight range",
        },
        {
            "name": "Unlimited",
            "description": "Unlimited range",
        },
    ]

    def __init__(
        self,
        repository: Type[SpellRangeTypeRepository] = SpellRangeTypeRepository,
    ) -> None:
        super().__init__(repository=repository)
