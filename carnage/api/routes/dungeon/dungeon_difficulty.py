from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.dungeon import (
    CreateDungeonDifficultySchema,
    ListDungeonDifficultySchema,
    UpdateDungeonDifficultySchema,
)
from carnage.database.repository.dungeon import DungeonDifficultyRepository


class DungeonDifficultyRoute(BaseRoute):
    list_schema = ListDungeonDifficultySchema
    create_schema = CreateDungeonDifficultySchema
    update_schema = UpdateDungeonDifficultySchema

    def __init__(
        self,
        name: str = "dungeon_difficulty",
        tags: list[str] = ["dungeon", "dungeon_difficulty"],
        repository: Type[
            DungeonDifficultyRepository
        ] = DungeonDifficultyRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListDungeonDifficultySchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListDungeonDifficultySchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateDungeonDifficultySchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateDungeonDifficultySchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = DungeonDifficultyRoute()
