"""Module to represent an Vocation schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationModel


class ListVocationSchema(
    sqlalchemy_to_pydantic(VocationModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateVocationSchema(
    sqlalchemy_to_pydantic(VocationModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateVocationSchema(
    sqlalchemy_to_pydantic(VocationModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
