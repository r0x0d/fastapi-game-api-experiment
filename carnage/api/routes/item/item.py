from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.item import (
    CreateItemSchema,
    ListItemSchema,
    UpdateItemSchema,
)
from carnage.database.repository.item import ItemRepository


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
