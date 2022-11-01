from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.size import SizeModel
from carnage.database.repository.size import SizeRepository
from carnage.routes.base import BaseRoute


class ListSizeSchema(
    sqlalchemy_to_pydantic(SizeModel),  # type: ignore
):
    pass


class UpdateSizeSchema(
    sqlalchemy_to_pydantic(SizeModel, config=None),  # type: ignore
):
    pass


class CreateSizeSchema(
    sqlalchemy_to_pydantic(SizeModel, config=None),  # type: ignore
):
    pass


class SizeRoute(BaseRoute):
    list_schema = ListSizeSchema
    create_schema = CreateSizeSchema
    update_schema = UpdateSizeSchema

    def __init__(
        self,
        name: str = "size",
        tags: list[str] = ["size"],
        repository: Type[SizeRepository] = SizeRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListSizeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSizeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSizeSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateSizeSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = SizeRoute()
