from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.spell import (
    CreateSpellSchema,
    ListSpellSchema,
    UpdateSpellSchema,
)
from carnage.database.repository.spell import SpellRepository


class SpellRoute(BaseRoute):
    list_schema = ListSpellSchema
    create_schema = CreateSpellSchema
    update_schema = UpdateSpellSchema

    def __init__(
        self,
        name: str = "spell",
        tags: list[str] = ["spell"],
        repository: Type[SpellRepository] = SpellRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListSpellSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSpellSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateSpellSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = SpellRoute()
