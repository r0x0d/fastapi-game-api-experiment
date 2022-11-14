from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.spell import (
    CreateSpellSchoolSchema,
    ListSpellSchoolSchema,
    UpdateSpellSchoolSchema,
)
from carnage.database.repository.spell import SpellSchoolRepository


class SpellSchoolRoute(BaseRoute):
    list_schema = ListSpellSchoolSchema
    create_schema = CreateSpellSchoolSchema
    update_schema = UpdateSpellSchoolSchema

    def __init__(
        self,
        name: str = "spell_school",
        tags: list[str] = ["spell", "spell-school"],
        repository: Type[SpellSchoolRepository] = SpellSchoolRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListSpellSchoolSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellSchoolSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSpellSchoolSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateSpellSchoolSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = SpellSchoolRoute()
