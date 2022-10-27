from typing import Type

from carnage.database.repository.spell_school import SpellSchoolRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.spell_school import (
    CreateSpellSchoolSchema,
    ListSpellSchoolSchema,
    UpdateSpellSchoolSchema,
)


class SpellSchoolRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell_school",
        tags: list[str] = ["spell", "spell-school"],
        repository: Type[SpellSchoolRepository] = SpellSchoolRepository,
        get_response_model: Type[
            ListSpellSchoolSchema
        ] = ListSpellSchoolSchema,
        post_response_model: Type[
            CreateSpellSchoolSchema
        ] = CreateSpellSchoolSchema,
        put_response_model: Type[
            UpdateSpellSchoolSchema
        ] = UpdateSpellSchoolSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


spell_school_route = SpellSchoolRoute()
