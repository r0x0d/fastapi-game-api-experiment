from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemRarityModel
from carnage.database.repository.item import ItemRarityRepository
from carnage.routes.base import BaseRoute

ListItemRaritySchema = sqlalchemy_to_pydantic(ItemRarityModel)
UpdateItemRaritySchema = sqlalchemy_to_pydantic(ItemRarityModel)
CreateItemRaritySchema = sqlalchemy_to_pydantic(ItemRarityModel)


class ItemRarityRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item_rarity",
        tags: list[str] = ["item", "item-rarity"],
        repository: Type[ItemRarityRepository] = ItemRarityRepository,
        get_response_model: BaseModel = ListItemRaritySchema,
        post_response_model: BaseModel = CreateItemRaritySchema,
        put_response_model: BaseModel = UpdateItemRaritySchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = ItemRarityRoute()
