from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemModel
from carnage.database.repository.item import ItemRepository
from carnage.routes.base import BaseRoute


class ListItemSchema(
    sqlalchemy_to_pydantic(ItemModel),  # type: ignore
):
    pass


class UpdateItemSchema(
    sqlalchemy_to_pydantic(ItemModel, config=None),  # type: ignore
):
    pass


class CreateItemSchema(
    sqlalchemy_to_pydantic(ItemModel, config=None),  # type: ignore
):
    pass


class ItemRoute(BaseRoute):
    list_schema = ListItemSchema
    create_schema = CreateItemSchema
    update_schema = UpdateItemSchema

    def __init__(
        self,
        name: str = "item",
        tags: list[str] = ["item"],
        repository: Type[ItemRepository] = ItemRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListItemSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListItemSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateItemSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateItemSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = ItemRoute()
