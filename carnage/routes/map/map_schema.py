from typing import Type

from pydantic import Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.dialects.postgresql import JSONB

from carnage.database.models.map import MapSchemaModel
from carnage.database.repository.map import MapSchemaRepository
from carnage.routes.base import BaseRoute

_ListMapSchemaSchema = sqlalchemy_to_pydantic(
    MapSchemaModel,
    exclude=("schema",),
)
_UpdateMapSchemaSchema = sqlalchemy_to_pydantic(
    MapSchemaModel,
    config=None,
    exclude=("schema",),
)
_CreateMapSchemaSchema = sqlalchemy_to_pydantic(
    MapSchemaModel,
    config=None,
    exclude=("schema",),
)


class ListMapSchemaSchema(_ListMapSchemaSchema):  # type: ignore
    _schema: JSONB = Field(alias="schema")


class CreateMapSchemaSchema(_CreateMapSchemaSchema):  # type: ignore
    _schema: JSONB = Field(alias="schema")


class UpdateMapSchemaSchema(_UpdateMapSchemaSchema):  # type: ignore
    _schema: JSONB = Field(alias="schema")


class MapSchemaRoute(BaseRoute):
    def __init__(
        self,
        name: str = "map_schema",
        tags: list[str] = ["map", "map_schema"],
        repository: Type[MapSchemaRepository] = MapSchemaRepository,
        get_response_model: Type[ListMapSchemaSchema] = ListMapSchemaSchema,
        post_response_model: Type[
            CreateMapSchemaSchema
        ] = CreateMapSchemaSchema,
        put_response_model: Type[
            UpdateMapSchemaSchema
        ] = UpdateMapSchemaSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = MapSchemaRoute()
