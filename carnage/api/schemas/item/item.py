"""Module to represent an Item schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemModel


class ListItemSchema(
    sqlalchemy_to_pydantic(ItemModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateItemSchema(
    sqlalchemy_to_pydantic(ItemModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateItemSchema(
    sqlalchemy_to_pydantic(ItemModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
