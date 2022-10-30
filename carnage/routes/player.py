from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.player import PlayerModel
from carnage.database.repository.player import PlayerRepository
from carnage.routes.base import BaseRoute

ListPlayerSchema = sqlalchemy_to_pydantic(PlayerModel)
UpdatePlayerSchema = sqlalchemy_to_pydantic(PlayerModel, config=None)
CreatePlayerSchema = sqlalchemy_to_pydantic(PlayerModel, config=None)


class PlayerRoute(BaseRoute):
    def __init__(
        self,
        name: str = "player",
        tags: list[str] = ["player"],
        repository: Type[PlayerRepository] = PlayerRepository,
        get_response_model: BaseModel = ListPlayerSchema,
        post_response_model: BaseModel = CreatePlayerSchema,
        put_response_model: BaseModel = UpdatePlayerSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = PlayerRoute()
