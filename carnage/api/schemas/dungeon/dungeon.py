"""Module to represent an Dungeon schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonModel


class ListDungeonSchema(
    sqlalchemy_to_pydantic(DungeonModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateDungeonSchema(
    sqlalchemy_to_pydantic(DungeonModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateDungeonSchema(
    sqlalchemy_to_pydantic(DungeonModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
