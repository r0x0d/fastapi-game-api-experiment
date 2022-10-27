from typing import Type

from carnage.database.repository.item_base_type import ItemBaseTypeRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.item_base_type import (
    CreateItemBaseTypeSchema,
    ListItemBaseTypeSchema,
    UpdateItemBaseTypeSchema,
)


class ItemBaseTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item_base_type",
        tags: list[str] = ["item", "item-base-type"],
        repository: Type[ItemBaseTypeRepository] = ItemBaseTypeRepository,
        get_response_model: Type[
            ListItemBaseTypeSchema
        ] = ListItemBaseTypeSchema,
        post_response_model: Type[
            CreateItemBaseTypeSchema
        ] = CreateItemBaseTypeSchema,
        put_response_model: Type[
            UpdateItemBaseTypeSchema
        ] = UpdateItemBaseTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


item_base_type_route = ItemBaseTypeRoute()
