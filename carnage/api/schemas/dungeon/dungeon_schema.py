from pydantic import Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonSchemaModel


class ListDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        exclude=("schema",),
    ),
):
    dungeon_schema: str = Field(alias="schema")


class CreateDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    dungeon_schema: str = Field(alias="schema")


class UpdateDungeonSchemaSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonSchemaModel,
        config=None,
        exclude=("schema",),
    ),
):
    dungeon_schema: str = Field(alias="schema")
