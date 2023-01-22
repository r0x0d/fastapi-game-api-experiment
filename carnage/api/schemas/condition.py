"""Module to represent an Condition schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.condition import ConditionModel


class ListConditionSchema(
    sqlalchemy_to_pydantic(ConditionModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateConditionSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ConditionModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateConditionSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ConditionModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
