from typing import Any, Type

from argon2 import PasswordHasher
from cryptography.fernet import Fernet

from carnage.database.models.account import ProviderEnum
from carnage.database.repository.account import AccountRepository
from carnage.database.seeds.base import BaseSeed

ph = PasswordHasher()


class AccountSeed(BaseSeed):
    name: str = "account"
    data: list[dict[str, str | Any]] = [
        {
            "username": "admin@carnage.io",
            "password": ph.hash("admin"),
            "provider": ProviderEnum.carnage,
            "secret_key": Fernet.generate_key(),
        },
    ]

    def __init__(
        self,
        repository: Type[AccountRepository] = AccountRepository,
    ) -> None:
        super().__init__(repository=repository)
