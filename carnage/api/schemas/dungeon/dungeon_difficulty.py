"""Module to represent an Dungeon Difficulty schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonDifficultyModel


class ListDungeonDifficultySchema(
    sqlalchemy_to_pydantic(DungeonDifficultyModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateDungeonDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonDifficultyModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateDungeonDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonDifficultyModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
