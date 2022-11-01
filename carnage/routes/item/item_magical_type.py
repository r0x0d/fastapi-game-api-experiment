from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemMagicalTypeModel
from carnage.database.repository.item import ItemMagicalTypeRepository
from carnage.routes.base import BaseRoute


class ListItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    pass


class UpdateItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    pass


class CreateItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    pass


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
            name,
            tags,
            repository,
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
