from typing import Type

from carnage.database.repository.spell_duration_type import (
    SpellDurationTypeRepository,
)
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.spell_duration_type import (
    CreateSpellDurationTypeSchema,
    ListSpellDurationTypeSchema,
    UpdateSpellDurationTypeSchema,
)


class SpellDurationTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell_duration_type",
        tags: list[str] = ["spell", "spell-duration-type"],
        repository: Type[
            SpellDurationTypeRepository
        ] = SpellDurationTypeRepository,
        get_response_model: Type[
            ListSpellDurationTypeSchema
        ] = ListSpellDurationTypeSchema,
        post_response_model: Type[
            CreateSpellDurationTypeSchema
        ] = CreateSpellDurationTypeSchema,
        put_response_model: Type[
            UpdateSpellDurationTypeSchema
        ] = UpdateSpellDurationTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


spell_duration_type_route = SpellDurationTypeRoute()
