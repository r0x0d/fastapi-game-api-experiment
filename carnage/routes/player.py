from typing import Type

from carnage.database.repository.player import PlayerRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.player import (
    CreatePlayerSchema,
    ListPlayerSchema,
    UpdatePlayerSchema,
)


class PlayerRoute(BaseRoute):
    def __init__(
        self,
        name: str = "player",
        tags: list[str] = ["player"],
        repository: Type[PlayerRepository] = PlayerRepository,
        get_response_model: Type[ListPlayerSchema] = ListPlayerSchema,
        post_response_model: Type[CreatePlayerSchema] = CreatePlayerSchema,
        put_response_model: Type[UpdatePlayerSchema] = UpdatePlayerSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


player_route = PlayerRoute()
