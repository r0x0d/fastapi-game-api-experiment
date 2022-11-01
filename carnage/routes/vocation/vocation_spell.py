from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationSpellModel
from carnage.database.repository.vocation import VocationSpellRepository
from carnage.routes.base import BaseRoute


class ListVocationSpellSchema(
    sqlalchemy_to_pydantic(VocationSpellModel),  # type: ignore
):
    pass


class UpdateVocationSpellSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        VocationSpellModel,
        config=None,
    ),
):
    pass


class CreateVocationSpellSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        VocationSpellModel,
        config=None,
    ),
):
    pass


class VocationSpellRoute(BaseRoute):
    list_schema = ListVocationSpellSchema
    create_schema = CreateVocationSpellSchema
    update_schema = UpdateVocationSpellSchema

    def __init__(
        self,
        name: str = "vocation_spell",
        tags: list[str] = ["vocation", "vocation-spell"],
        repository: Type[VocationSpellRepository] = VocationSpellRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListVocationSpellSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListVocationSpellSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateVocationSpellSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateVocationSpellSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = VocationSpellRoute()
