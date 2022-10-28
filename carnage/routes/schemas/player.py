from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.player import PlayerModel

ListPlayerSchema = sqlalchemy_to_pydantic(PlayerModel)
UpdatePlayerSchema = sqlalchemy_to_pydantic(PlayerModel, config=None)
CreatePlayerSchema = sqlalchemy_to_pydantic(PlayerModel, config=None)
