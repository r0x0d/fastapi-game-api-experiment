from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.race import RaceModel
from carnage.database.repository.race import RaceRepository
from carnage.routes.base import BaseRoute


class ListRaceSchema(
    sqlalchemy_to_pydantic(RaceModel),  # type: ignore
):
    pass


class UpdateRaceSchema(
    sqlalchemy_to_pydantic(RaceModel, config=None),  # type: ignore
):
    pass


class CreateRaceSchema(
    sqlalchemy_to_pydantic(RaceModel, config=None),  # type: ignore
):
    pass


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
            name,
            tags,
            repository,
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
