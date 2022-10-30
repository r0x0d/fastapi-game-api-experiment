from typing import Type

from carnage.database.models.spell import SpellSchoolModel
from carnage.database.repository.base import BaseRepository


class SpellSchoolRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SpellSchoolModel] = SpellSchoolModel,
    ) -> None:
        super().__init__(model)
