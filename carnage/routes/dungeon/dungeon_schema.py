from typing import Type

from pydantic import Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.dialects.postgresql import JSONB

from carnage.database.models.dungeon import DungeonSchemaModel
from carnage.database.repository.dungeon import DungeonSchemaRepository
from carnage.routes.base import BaseRoute


class ListDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        exclude=("schema",),
    ),
):
    _schema: JSONB = Field(alias="schema")


class CreateDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    _schema: JSONB = Field(alias="schema")


class UpdateDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    _schema: JSONB = Field(alias="schema")


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
