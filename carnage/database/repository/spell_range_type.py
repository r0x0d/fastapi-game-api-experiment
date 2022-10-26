from typing import Type

from carnage.database.models.spell_range_type import SpellRangeTypeModel
from carnage.database.repository.base import BaseRepository


class SpellRangeTypeRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SpellRangeTypeModel] = SpellRangeTypeModel,
    ) -> None:
        super().__init__(model)
