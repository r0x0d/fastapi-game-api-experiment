"""Module to represent an Spell Range Type schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellRangeTypeModel


class ListSpellRangeTypeSchema(
    sqlalchemy_to_pydantic(SpellRangeTypeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateSpellRangeTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellRangeTypeModel,
        config=None,
    ),
):
    """Class that represents an update of elements."""


class CreateSpellRangeTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellRangeTypeModel,
        config=None,
    ),
):
    """Class that represents an creation of elements."""
