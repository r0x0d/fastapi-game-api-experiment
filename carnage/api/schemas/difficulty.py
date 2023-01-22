"""Module to represent an Difficulty schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.difficulty import DifficultyModel


class ListDifficultySchema(
    sqlalchemy_to_pydantic(DifficultyModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateDifficultySchema(
    sqlalchemy_to_pydantic(DifficultyModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateDifficultySchema(
    sqlalchemy_to_pydantic(DifficultyModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
