from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.game_mode import GameModeModel


class ListGameModeSchema(
    sqlalchemy_to_pydantic(GameModeModel),  # type: ignore
):
    pass


class UpdateGameModeSchema(
    sqlalchemy_to_pydantic(GameModeModel, config=None),  # type: ignore
):
    pass


class CreateGameModeSchema(
    sqlalchemy_to_pydantic(GameModeModel, config=None),  # type: ignore
):
    pass
