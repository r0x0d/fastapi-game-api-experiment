"""Module to represent an Player schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.player import PlayerModel


class ListPlayerSchema(
    sqlalchemy_to_pydantic(PlayerModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdatePlayerSchema(
    sqlalchemy_to_pydantic(PlayerModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreatePlayerSchema(
    sqlalchemy_to_pydantic(PlayerModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
