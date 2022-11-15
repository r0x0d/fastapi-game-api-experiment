from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.item import (
    CreateItemMagicalTypeSchema,
    ListItemMagicalTypeSchema,
    UpdateItemMagicalTypeSchema,
)
from carnage.database.repository.item import ItemMagicalTypeRepository


class ItemMagicalTypeRoute(BaseRoute):
    list_schema = ListItemMagicalTypeSchema
    create_schema = CreateItemMagicalTypeSchema
    update_schema = UpdateItemMagicalTypeSchema

    def __init__(
        self,
        name: str = "item_magical_type",
        tags: list[str] = ["item", "item-magical-type"],
        repository: Type[
            ItemMagicalTypeRepository
        ] = ItemMagicalTypeRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListItemMagicalTypeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListItemMagicalTypeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateItemMagicalTypeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateItemMagicalTypeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = ItemMagicalTypeRoute()
