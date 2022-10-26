from typing import Type

from carnage.database.repository.spell_duration_type import (
    SpellDurationTypeRepository,
)
from carnage.database.seeds.base import BaseSeed


class SpellDurationTypeSeed(BaseSeed):
    name: str = "spell-duration-type"
    data: list[dict[str, str]] = [
        {
            "name": "Concentration",
            "description": "Concentration duration",
        },
        {
            "name": "Instantaneous",
            "description": "Instantaneous duration",
        },
        {
            "name": "Special",
            "description": "Special duration",
        },
        {
            "name": "Time",
            "description": "Time duration",
        },
        {
            "name": "Until Dispelled",
            "description": "Until Dispelled duration",
        },
        {
            "name": "Until Dispelled or Triggered",
            "description": "Until Dispelled or Triggered duration",
        },
    ]

    def __init__(
        self,
        repository: Type[
            SpellDurationTypeRepository
        ] = SpellDurationTypeRepository,
    ) -> None:
        super().__init__(repository=repository)
