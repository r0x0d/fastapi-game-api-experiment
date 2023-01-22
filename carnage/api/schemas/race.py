"""Module to represent an Race schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.race import RaceModel


class ListRaceSchema(
    sqlalchemy_to_pydantic(RaceModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateRaceSchema(
    sqlalchemy_to_pydantic(RaceModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateRaceSchema(
    sqlalchemy_to_pydantic(RaceModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
