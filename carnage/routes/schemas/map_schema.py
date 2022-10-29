from pydantic import Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.dialects.postgresql import JSONB

from carnage.database.models.map_schema import MapSchemaModel

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
