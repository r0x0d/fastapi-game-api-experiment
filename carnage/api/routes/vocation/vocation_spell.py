from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.vocation import (
    CreateVocationSpellSchema,
    ListVocationSpellSchema,
    UpdateVocationSpellSchema,
)
from carnage.database.repository.vocation import VocationSpellRepository


class VocationSpellRoute(BaseRoute):
    list_schema = ListVocationSpellSchema
    create_schema = CreateVocationSpellSchema
    update_schema = UpdateVocationSpellSchema

    def __init__(
        self,
        name: str = "vocation_spell",
        tags: list[str] = ["vocation", "vocation-spell"],
        repository: Type[VocationSpellRepository] = VocationSpellRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListVocationSpellSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListVocationSpellSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateVocationSpellSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateVocationSpellSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = VocationSpellRoute()
