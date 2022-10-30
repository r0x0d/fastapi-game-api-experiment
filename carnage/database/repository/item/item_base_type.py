from typing import Type

from carnage.database.models.item.item_base_type import ItemBaseTypeModel
from carnage.database.repository.base import BaseRepository


class ItemBaseTypeRepository(BaseRepository):
    def __init__(
        self,
        model: Type[ItemBaseTypeModel] = ItemBaseTypeModel,
    ) -> None:
        super().__init__(model)
