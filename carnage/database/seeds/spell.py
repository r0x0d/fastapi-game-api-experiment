from typing import Any, Type

from carnage.database.repository.spell import SpellRepository
from carnage.database.repository.spell_duration_type import (
    SpellDurationTypeRepository,
)
from carnage.database.repository.spell_range_type import (
    SpellRangeTypeRepository,
)
from carnage.database.repository.spell_school import SpellSchoolRepository
from carnage.database.seeds.base import BaseSeed


class SpellSeed(BaseSeed):
    name: str = "spell"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
        },
    ]

    def __init__(
        self,
        repository: Type[SpellRepository] = SpellRepository,
    ) -> None:
        super().__init__(repository=repository)
        self.spell_school_repository = SpellSchoolRepository()
        self.spell_duration_type_repository = SpellDurationTypeRepository()
        self.spell_range_type_repository = SpellRangeTypeRepository()

    def seed(self) -> None:
        spell_school = self.spell_school_repository.select_first()
        spell_duration_type = (
            self.spell_duration_type_repository.select_first()
        )
        spell_range_type = self.spell_range_type_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "spell_school_id": spell_school[0].id,
                    "spell_duration_type_id": spell_duration_type[0].id,
                    "spell_range_type_id": spell_range_type[0].id,
                },
            )

        super().seed()
