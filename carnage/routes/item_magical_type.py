from typing import Type

from carnage.database.repository.item_magical_type import (
    ItemMagicalTypeRepository,
)
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.item_magical_type import (
    CreateItemMagicalTypeSchema,
    ListItemMagicalTypeSchema,
    UpdateItemMagicalTypeSchema,
)


class ItemMagicalTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "item_magical_type",
        tags: list[str] = ["item", "item-magical-type"],
        repository: Type[
            ItemMagicalTypeRepository
        ] = ItemMagicalTypeRepository,
        get_response_model: Type[
            ListItemMagicalTypeSchema
        ] = ListItemMagicalTypeSchema,
        post_response_model: Type[
            CreateItemMagicalTypeSchema
        ] = CreateItemMagicalTypeSchema,
        put_response_model: Type[
            UpdateItemMagicalTypeSchema
        ] = UpdateItemMagicalTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


item_magical_type_route = ItemMagicalTypeRoute()
