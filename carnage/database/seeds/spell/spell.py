from typing import Any

from carnage.database.repository.spell import (
    SpellDurationTypeRepository,
    SpellRangeTypeRepository,
    SpellRepository,
    SpellSchoolRepository,
)
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
        repository: type[SpellRepository] = SpellRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.spell_school_repository = SpellSchoolRepository()
        self.spell_duration_type_repository = SpellDurationTypeRepository()
        self.spell_range_type_repository = SpellRangeTypeRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
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
