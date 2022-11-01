from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemBaseTypeModel
from carnage.database.repository.item import ItemBaseTypeRepository
from carnage.routes.base import BaseRoute


class ListItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    pass


class UpdateItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    pass


class CreateItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    pass


class ItemBaseTypeRoute(BaseRoute):
    list_schema = ListItemBaseTypeSchema
    create_schema = CreateItemBaseTypeSchema
    update_schema = UpdateItemBaseTypeSchema

    def __init__(
        self,
        name: str = "item_base_type",
        tags: list[str] = ["item", "item-base-type"],
        repository: Type[ItemBaseTypeRepository] = ItemBaseTypeRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListItemBaseTypeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListItemBaseTypeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateItemBaseTypeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateItemBaseTypeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = ItemBaseTypeRoute()
