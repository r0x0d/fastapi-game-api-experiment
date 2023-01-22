"""Module to represent an Monster schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster import MonsterModel


class ListMonsterSchema(
    sqlalchemy_to_pydantic(MonsterModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateMonsterSchema(
    sqlalchemy_to_pydantic(MonsterModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateMonsterSchema(
    sqlalchemy_to_pydantic(MonsterModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
