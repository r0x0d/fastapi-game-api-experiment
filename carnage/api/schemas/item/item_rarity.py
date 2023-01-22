"""Module to represent an Item Rarity schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemRarityModel


class ListItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    """Class that represents an creation of elements."""
