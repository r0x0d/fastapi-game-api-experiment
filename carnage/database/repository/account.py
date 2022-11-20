from typing import Type

from sqlalchemy import select

from carnage.database.models.account import AccountModel
from carnage.database.repository.base import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(
        self,
        model: Type[AccountModel] = AccountModel,
    ) -> None:
        super().__init__(model)

    def select_by_username(self, username: str) -> AccountModel:
        statement = select(self.model).where(self.model.username == username)

        with self.session() as session:
            return session.execute(statement=statement).first()

    def select_by_nickname(self, nickname: str) -> AccountModel:
        statement = select(self.model).where(self.model.nickname == nickname)

        with self.session() as session:
            return session.execute(statement=statement).first()
