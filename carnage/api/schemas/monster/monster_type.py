"""Module to represent an Monster Type schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster.monster_type import MonsterTypeModel


class ListMonsterTypeSchema(
    sqlalchemy_to_pydantic(MonsterTypeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateMonsterTypeSchema(
    sqlalchemy_to_pydantic(MonsterTypeModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateMonsterTypeSchema(
    sqlalchemy_to_pydantic(MonsterTypeModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
