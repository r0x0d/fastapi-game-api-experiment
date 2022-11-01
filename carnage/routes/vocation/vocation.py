from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationModel
from carnage.database.repository.vocation import VocationRepository
from carnage.routes.base import BaseRoute


class ListVocationSchema(
    sqlalchemy_to_pydantic(VocationModel),  # type: ignore
):
    pass


class UpdateVocationSchema(
    sqlalchemy_to_pydantic(VocationModel, config=None),  # type: ignore
):
    pass


class CreateVocationSchema(
    sqlalchemy_to_pydantic(VocationModel, config=None),  # type: ignore
):
    pass


class VocationRoute(BaseRoute):
    list_schema = ListVocationSchema
    create_schema = CreateVocationSchema
    update_schema = UpdateVocationSchema

    def __init__(
        self,
        name: str = "vocation",
        tags: list[str] = ["vocation"],
        repository: Type[VocationRepository] = VocationRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListVocationSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListVocationSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateVocationSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateVocationSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = VocationRoute()
