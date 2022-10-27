from typing import Type

from carnage.database.repository.item_rarity import ItemRarityRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.item_rarity import (
    CreateItemRaritySchema,
    ListItemRaritySchema,
    UpdateItemRaritySchema,
)


class ItemRarityRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item_rarity",
        tags: list[str] = ["item", "item-rarity"],
        repository: Type[ItemRarityRepository] = ItemRarityRepository,
        get_response_model: Type[ListItemRaritySchema] = ListItemRaritySchema,
        post_response_model: Type[
            CreateItemRaritySchema
        ] = CreateItemRaritySchema,
        put_response_model: Type[
            UpdateItemRaritySchema
        ] = UpdateItemRaritySchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


item_rarity_route = ItemRarityRoute()
