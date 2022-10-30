from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemModel
from carnage.database.repository.item import ItemRepository
from carnage.routes.base import BaseRoute

ListItemSchema = sqlalchemy_to_pydantic(ItemModel)
UpdateItemSchema = sqlalchemy_to_pydantic(ItemModel, config=None)
CreateItemSchema = sqlalchemy_to_pydantic(ItemModel, config=None)


class ItemRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item",
        tags: list[str] = ["item"],
        repository: Type[ItemRepository] = ItemRepository,
        get_response_model: BaseModel = ListItemSchema,
        post_response_model: BaseModel = CreateItemSchema,
        put_response_model: BaseModel = UpdateItemSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = ItemRoute()
