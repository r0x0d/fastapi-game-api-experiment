from typing import Type

from carnage.database.models.setting import SettingModel
from carnage.database.repository.base import BaseRepository


class SettingRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SettingModel] = SettingModel,
    ) -> None:
        super().__init__(model)
