"""Module to represent an Size schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.size import SizeModel


class ListSizeSchema(
    sqlalchemy_to_pydantic(SizeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateSizeSchema(
    sqlalchemy_to_pydantic(SizeModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateSizeSchema(
    sqlalchemy_to_pydantic(SizeModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
