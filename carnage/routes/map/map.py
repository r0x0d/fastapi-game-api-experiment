from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.map import MapModel
from carnage.database.repository.map import MapRepository
from carnage.routes.base import BaseRoute


class ListMapSchema(
    sqlalchemy_to_pydantic(MapModel),  # type: ignore
):
    pass


class UpdateMapSchema(
    sqlalchemy_to_pydantic(MapModel, config=None),  # type: ignore
):
    pass


class CreateMapSchema(
    sqlalchemy_to_pydantic(MapModel, config=None),  # type: ignore
):
    pass


class MapRoute(BaseRoute):
    list_schema = ListMapSchema
    create_schema = CreateMapSchema
    update_schema = UpdateMapSchema

    def __init__(
        self,
        name: str = "map",
        tags: list[str] = ["map"],
        repository: Type[MapRepository] = MapRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListMapSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMapSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateMapSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateMapSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = MapRoute()
