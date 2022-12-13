from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.game_mode import (
    CreateGameModeSchema,
    ListGameModeSchema,
    UpdateGameModeSchema,
)
from carnage.database.repository.game_mode import GameModeRepository


class GameModeRoute(BaseRoute):
    list_schema = ListGameModeSchema
    update_schema = CreateGameModeSchema
    create_schema = UpdateGameModeSchema

    def __init__(
        self,
        name: str = "game_mode",
        tags: list[str] = ["game-mode"],
        repository: Type[GameModeRepository] = GameModeRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListGameModeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListGameModeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateGameModeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateGameModeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = GameModeRoute()
