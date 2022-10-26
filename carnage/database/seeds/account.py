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

    def validate_seed(self, seed: dict[str, str]) -> bool:
        print(f"Validating the current seed with username: {seed['username']}")

        result = self.repository.select_by_username(  # type: ignore
            username=seed["username"],
        )
        if result:
            print("Seed already exists in the database")
            return True

        return False

    def __init__(
        self,
        repository: Type[AccountRepository] = AccountRepository,
    ) -> None:
        super().__init__(repository=repository)
