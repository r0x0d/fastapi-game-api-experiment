"""Module to represent an Spell School schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellSchoolModel


class ListSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
