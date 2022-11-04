from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.player import (
    CreatePlayerSchema,
    ListPlayerSchema,
    UpdatePlayerSchema,
)
from carnage.database.repository.player import PlayerRepository


class PlayerRoute(BaseRoute):
    list_schema = ListPlayerSchema
    create_schema = CreatePlayerSchema
    update_schema = UpdatePlayerSchema

    def __init__(
        self,
        name: str = "player",
        tags: list[str] = ["player"],
        repository: Type[PlayerRepository] = PlayerRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListPlayerSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListPlayerSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreatePlayerSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdatePlayerSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = PlayerRoute()
