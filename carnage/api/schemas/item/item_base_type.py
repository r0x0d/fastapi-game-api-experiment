"""Module to represent an Item Base Type schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemBaseTypeModel


class ListItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    """Class that represents an creation of elements."""
