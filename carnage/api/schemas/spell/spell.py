"""Module to represent an Spell schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellModel


class ListSpellSchema(
    sqlalchemy_to_pydantic(SpellModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateSpellSchema(
    sqlalchemy_to_pydantic(SpellModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateSpellSchema(
    sqlalchemy_to_pydantic(SpellModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
