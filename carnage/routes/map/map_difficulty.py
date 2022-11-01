from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.map import MapDifficultyModel
from carnage.database.repository.map import MapDifficultyRepository
from carnage.routes.base import BaseRoute


class ListMapDifficultySchema(
    sqlalchemy_to_pydantic(MapDifficultyModel),  # type: ignore
):
    pass


class UpdateMapDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        MapDifficultyModel,
        config=None,
    ),
):
    pass


class CreateMapDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        MapDifficultyModel,
        config=None,
    ),
):
    pass


class MapDifficultyRoute(BaseRoute):
    list_schema = ListMapDifficultySchema
    create_schema = CreateMapDifficultySchema
    update_schema = UpdateMapDifficultySchema

    def __init__(
        self,
        name: str = "map_difficulty",
        tags: list[str] = ["map", "map_difficulty"],
        repository: Type[MapDifficultyRepository] = MapDifficultyRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListMapDifficultySchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMapDifficultySchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateMapDifficultySchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateMapDifficultySchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = MapDifficultyRoute()
