from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.race import (
    CreateRaceSchema,
    ListRaceSchema,
    UpdateRaceSchema,
)
from carnage.database.repository.race import RaceRepository


class RaceRoute(BaseRoute):
    list_schema = ListRaceSchema
    update_schema = CreateRaceSchema
    create_schema = UpdateRaceSchema

    def __init__(
        self,
        name: str = "race",
        tags: list[str] = ["race"],
        repository: Type[RaceRepository] = RaceRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListRaceSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListRaceSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateRaceSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateRaceSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = RaceRoute()
