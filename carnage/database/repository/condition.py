from typing import Type

from carnage.database.models.condition import ConditionModel
from carnage.database.repository.base import BaseRepository


class ConditionRepository(BaseRepository):
    def __init__(
        self,
        model: Type[ConditionModel] = ConditionModel,
    ) -> None:
        super().__init__(model)
