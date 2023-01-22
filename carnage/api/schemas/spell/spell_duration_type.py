"""Module to represent an Spell Duration Type schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellDurationTypeModel


class ListSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(SpellDurationTypeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellDurationTypeModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellDurationTypeModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
