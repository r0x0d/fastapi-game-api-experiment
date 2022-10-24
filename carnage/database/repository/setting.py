from typing import Type

from sqlalchemy import select

from carnage.database.models.setting import SettingModel
from carnage.database.repository.base import BaseRepository


class SettingRepository(BaseRepository):
    def __init__(
        self,
        model: Type[SettingModel] = SettingModel,
    ) -> None:
        super().__init__(model)

    def select_by_environment(
        self,
        environment: str = "production",
    ) -> SettingModel:
        statement = select(self.model).where(
            self.model.environment == environment,
        )
        with self.session() as session:
            return session.execute(statement=statement).first()
