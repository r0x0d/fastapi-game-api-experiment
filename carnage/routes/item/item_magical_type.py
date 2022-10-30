from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemMagicalTypeModel
from carnage.database.repository.item import ItemMagicalTypeRepository
from carnage.routes.base import BaseRoute

ListItemMagicalTypeSchema = sqlalchemy_to_pydantic(ItemMagicalTypeModel)
UpdateItemMagicalTypeSchema = sqlalchemy_to_pydantic(ItemMagicalTypeModel)
CreateItemMagicalTypeSchema = sqlalchemy_to_pydantic(ItemMagicalTypeModel)


class ItemMagicalTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item_magical_type",
        tags: list[str] = ["item", "item-magical-type"],
        repository: Type[
            ItemMagicalTypeRepository
        ] = ItemMagicalTypeRepository,
        get_response_model: BaseModel = ListItemMagicalTypeSchema,
        post_response_model: BaseModel = CreateItemMagicalTypeSchema,
        put_response_model: BaseModel = UpdateItemMagicalTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = ItemMagicalTypeRoute()
