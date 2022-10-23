from typing import Type

from carnage.database.models.account import AccountModel
from carnage.database.repository.base import BaseRepository


class AccountRepository(BaseRepository):
    def __init__(
        self,
        model: Type[AccountModel] = AccountModel,
    ) -> None:
        super().__init__(model)
