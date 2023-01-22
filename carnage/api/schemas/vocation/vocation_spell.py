"""Module to represent an Vocation Spell schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationSpellModel


class ListVocationSpellSchema(
    sqlalchemy_to_pydantic(VocationSpellModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateVocationSpellSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        VocationSpellModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateVocationSpellSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        VocationSpellModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
