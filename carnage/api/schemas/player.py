from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.player import PlayerModel


class ListPlayerSchema(
    sqlalchemy_to_pydantic(PlayerModel),  # type: ignore
):
    pass


class UpdatePlayerSchema(
    sqlalchemy_to_pydantic(PlayerModel, config=None),  # type: ignore
):
    pass


class CreatePlayerSchema(
    sqlalchemy_to_pydantic(PlayerModel, config=None),  # type: ignore
):
    pass
