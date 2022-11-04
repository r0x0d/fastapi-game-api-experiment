from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.dungeon import (
    CreateDungeonSchema,
    ListDungeonSchema,
    UpdateDungeonSchema,
)
from carnage.database.repository.dungeon import DungeonRepository


class DungeonRoute(BaseRoute):
    list_schema = ListDungeonSchema
    create_schema = CreateDungeonSchema
    update_schema = UpdateDungeonSchema

    def __init__(
        self,
        name: str = "dungeon",
        tags: list[str] = ["dungeon"],
        repository: Type[DungeonRepository] = DungeonRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListDungeonSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListDungeonSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateDungeonSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateDungeonSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = DungeonRoute()
