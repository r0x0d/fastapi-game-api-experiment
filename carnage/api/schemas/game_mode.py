"""Module to represent an Game Mode schema."""

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.game_mode import GameModeModel


class ListGameModeSchema(
    sqlalchemy_to_pydantic(GameModeModel),  # type: ignore
):
    """Class that represents a listing of elements."""


class UpdateGameModeSchema(
    sqlalchemy_to_pydantic(GameModeModel, config=None),  # type: ignore
):
    """Class that represents an update of elements."""


class CreateGameModeSchema(
    sqlalchemy_to_pydantic(GameModeModel, config=None),  # type: ignore
):
    """Class that represents an creation of elements."""
