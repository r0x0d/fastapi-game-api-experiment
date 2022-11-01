from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonModel
from carnage.database.repository.dungeon import DungeonRepository
from carnage.routes.base import BaseRoute


class ListDungeonSchema(
    sqlalchemy_to_pydantic(DungeonModel),  # type: ignore
):
    pass


class UpdateDungeonSchema(
    sqlalchemy_to_pydantic(DungeonModel, config=None),  # type: ignore
):
    pass


class CreateDungeonSchema(
    sqlalchemy_to_pydantic(DungeonModel, config=None),  # type: ignore
):
    pass


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
