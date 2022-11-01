from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.player import PlayerModel
from carnage.database.repository.player import PlayerRepository
from carnage.routes.base import BaseRoute


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
