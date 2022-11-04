from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.spell import (
    CreateSpellRangeTypeSchema,
    ListSpellRangeTypeSchema,
    UpdateSpellRangeTypeSchema,
)
from carnage.database.repository.spell import SpellRangeTypeRepository


class SpellRangeTypeRoute(BaseRoute):
    list_schema = ListSpellRangeTypeSchema
    create_schema = CreateSpellRangeTypeSchema
    update_schema = UpdateSpellRangeTypeSchema

    def __init__(
        self,
        name: str = "spell_range_type",
        tags: list[str] = ["spell", "spell-range-type"],
        repository: Type[SpellRangeTypeRepository] = SpellRangeTypeRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListSpellRangeTypeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellRangeTypeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSpellRangeTypeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateSpellRangeTypeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = SpellRangeTypeRoute()
