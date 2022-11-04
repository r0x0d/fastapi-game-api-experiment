from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.dungeon import (
    CreateDungeonSchemaSchema,
    ListDungeonSchemaSchema,
    UpdateDungeonSchemaSchema,
)
from carnage.database.repository.dungeon import DungeonSchemaRepository


class DungeonSchemaRoute(BaseRoute):
    list_schema = ListDungeonSchemaSchema
    create_schema = CreateDungeonSchemaSchema
    update_schema = UpdateDungeonSchemaSchema

    def __init__(
        self,
        name: str = "dungeon_schema",
        tags: list[str] = ["dungeon", "dungeon_schema"],
        repository: Type[DungeonSchemaRepository] = DungeonSchemaRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListDungeonSchemaSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListDungeonSchemaSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateDungeonSchemaSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateDungeonSchemaSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = DungeonSchemaRoute()
