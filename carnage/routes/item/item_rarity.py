from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemRarityModel
from carnage.database.repository.item import ItemRarityRepository
from carnage.routes.base import BaseRoute


class ListItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    pass


class UpdateItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    pass


class CreateItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    pass


class ItemRarityRoute(BaseRoute):
    list_schema = ListItemRaritySchema
    create_schema = CreateItemRaritySchema
    update_schema = UpdateItemRaritySchema

    def __init__(
        self,
        name: str = "item_rarity",
        tags: list[str] = ["item", "item-rarity"],
        repository: Type[ItemRarityRepository] = ItemRarityRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListItemRaritySchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListItemRaritySchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateItemRaritySchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateItemRaritySchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = ItemRarityRoute()
