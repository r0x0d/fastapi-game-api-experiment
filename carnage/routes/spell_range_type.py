from typing import Type

from carnage.database.repository.spell_range_type import (
    SpellRangeTypeRepository,
)
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.spell_range_type import (
    CreateSpellRangeTypeSchema,
    ListSpellRangeTypeSchema,
    UpdateSpellRangeTypeSchema,
)


class SpellRangeTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell_range_type",
        tags: list[str] = ["spell", "spell-range-type"],
        repository: Type[SpellRangeTypeRepository] = SpellRangeTypeRepository,
        get_response_model: Type[
            ListSpellRangeTypeSchema
        ] = ListSpellRangeTypeSchema,
        post_response_model: Type[
            CreateSpellRangeTypeSchema
        ] = CreateSpellRangeTypeSchema,
        put_response_model: Type[
            UpdateSpellRangeTypeSchema
        ] = UpdateSpellRangeTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


spell_range_type_route = SpellRangeTypeRoute()
