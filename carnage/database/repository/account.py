from functools import lru_cache
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

    @lru_cache
    def select_by_username(self, username: str) -> AccountModel:
        statement = select(self.model).where(
            self.model.username == username
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()

    @lru_cache
    def select_by_nickname(self, nickname: str) -> AccountModel:
        statement = select(self.model).where(
            self.model.nickname == nickname
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()
