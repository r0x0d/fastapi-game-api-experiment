from typing import Type

from carnage.database.repository.item import ItemRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.item import (
    CreateItemSchema,
    ListItemSchema,
    UpdateItemSchema,
)


class ItemRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item",
        tags: list[str] = ["item"],
        repository: Type[ItemRepository] = ItemRepository,
        get_response_model: Type[ListItemSchema] = ListItemSchema,
        post_response_model: Type[CreateItemSchema] = CreateItemSchema,
        put_response_model: Type[UpdateItemSchema] = UpdateItemSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


item_route = ItemRoute()
