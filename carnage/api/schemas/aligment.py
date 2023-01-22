"""Module to represent an Aligment schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.aligment import AligmentModel


class ListAligmentSchema(
    sqlalchemy_to_pydantic(AligmentModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
