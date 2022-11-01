from typing import Type

from pydantic import Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.dialects.postgresql import JSONB

from carnage.database.models.map import MapSchemaModel
from carnage.database.repository.map import MapSchemaRepository
from carnage.routes.base import BaseRoute


class ListMapSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        MapSchemaModel,
        exclude=("schema",),
    ),
):
    _schema: JSONB = Field(alias="schema")


class CreateMapSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        MapSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    _schema: JSONB = Field(alias="schema")


class UpdateMapSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        MapSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    _schema: JSONB = Field(alias="schema")


class MapSchemaRoute(BaseRoute):
    list_schema = ListMapSchemaSchema
    create_schema = CreateMapSchemaSchema
    update_schema = UpdateMapSchemaSchema

    def __init__(
        self,
        name: str = "map_schema",
        tags: list[str] = ["map", "map_schema"],
        repository: Type[MapSchemaRepository] = MapSchemaRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListMapSchemaSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMapSchemaSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateMapSchemaSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateMapSchemaSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = MapSchemaRoute()
