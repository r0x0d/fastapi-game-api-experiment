from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.spell import (
    CreateSpellDurationTypeSchema,
    ListSpellDurationTypeSchema,
    UpdateSpellDurationTypeSchema,
)
from carnage.database.repository.spell import SpellDurationTypeRepository


class SpellDurationTypeRoute(BaseRoute):
    list_schema = ListSpellDurationTypeSchema
    create_schema = CreateSpellDurationTypeSchema
    update_schema = UpdateSpellDurationTypeSchema

    def __init__(
        self,
        name: str = "spell_duration_type",
        tags: list[str] = ["spell", "spell-duration-type"],
        repository: Type[
            SpellDurationTypeRepository
        ] = SpellDurationTypeRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListSpellDurationTypeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellDurationTypeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSpellDurationTypeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateSpellDurationTypeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = SpellDurationTypeRoute()
