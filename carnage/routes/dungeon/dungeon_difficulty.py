from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonDifficultyModel
from carnage.database.repository.dungeon import DungeonDifficultyRepository
from carnage.routes.base import BaseRoute


class ListDungeonDifficultySchema(
    sqlalchemy_to_pydantic(DungeonDifficultyModel),  # type: ignore
):
    pass


class UpdateDungeonDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonDifficultyModel,
        config=None,
    ),
):
    pass


class CreateDungeonDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonDifficultyModel,
        config=None,
    ),
):
    pass


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
