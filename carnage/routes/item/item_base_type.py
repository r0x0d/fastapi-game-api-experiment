from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemBaseTypeModel
from carnage.database.repository.item import ItemBaseTypeRepository
from carnage.routes.base import BaseRoute

ListItemBaseTypeSchema = sqlalchemy_to_pydantic(ItemBaseTypeModel)
UpdateItemBaseTypeSchema = sqlalchemy_to_pydantic(ItemBaseTypeModel)
CreateItemBaseTypeSchema = sqlalchemy_to_pydantic(ItemBaseTypeModel)


class ItemBaseTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item_base_type",
        tags: list[str] = ["item", "item-base-type"],
        repository: Type[ItemBaseTypeRepository] = ItemBaseTypeRepository,
        get_response_model: BaseModel = ListItemBaseTypeSchema,
        post_response_model: BaseModel = CreateItemBaseTypeSchema,
        put_response_model: BaseModel = UpdateItemBaseTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = ItemBaseTypeRoute()
