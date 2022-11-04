from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonModel


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
