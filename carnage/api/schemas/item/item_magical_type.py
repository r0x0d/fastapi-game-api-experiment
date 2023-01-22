"""Module to represent an Item Magical Type schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemMagicalTypeModel


class ListItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    """Class that represents an creation of elements."""
