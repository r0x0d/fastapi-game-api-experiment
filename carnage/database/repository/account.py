"""Module that represents the Account repository."""
from functools import lru_cache

from sqlalchemy import select

from carnage.database.models.account import AccountModel
from carnage.database.repository.base import BaseRepository


class AccountRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[AccountModel] = AccountModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)

    @lru_cache
    def select_by_username(self, username: str) -> AccountModel:
        """Get results from database filtering by username.

        :param username: Username to be used in the filter.
        """
        statement = select(self.model).where(
            self.model.username == username
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()

    @lru_cache
    def select_by_nickname(self, nickname: str) -> AccountModel:
        """Get results from database filtering by nickname.

        :param nickanem: Nickname to be used in the filter.
        """
        statement = select(self.model).where(
            self.model.nickname == nickname
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()
