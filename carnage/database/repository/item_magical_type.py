from typing import Type

from carnage.database.models.item_magical_type import ItemMagicalTypeModel
from carnage.database.repository.base import BaseRepository


class ItemMagicalTypeRepository(BaseRepository):
    def __init__(
        self,
        model: Type[ItemMagicalTypeModel] = ItemMagicalTypeModel,
    ) -> None:
        super().__init__(model)
