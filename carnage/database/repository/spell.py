from typing import Type

from carnage.database.models.spell import SpellModel
from carnage.database.repository.base import BaseRepository


class SpellRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SpellModel] = SpellModel,
    ) -> None:
        super().__init__(model)
