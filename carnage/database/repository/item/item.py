from typing import Type

from carnage.database.models.item import ItemModel
from carnage.database.repository.base import BaseRepository


class ItemRepository(BaseRepository):
    def __init__(self, model: Type[ItemModel] = ItemModel) -> None:
        super().__init__(model)
