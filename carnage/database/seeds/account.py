import logging
from typing import Any

from cryptography.fernet import Fernet

from carnage.database.models.account import ProviderEnum
from carnage.database.repository.account import AccountRepository
from carnage.database.seeds.base import BaseSeed

logger = logging.getLogger(__name__)


class AccountSeed(BaseSeed):
    name: str = "account"
    data: list[dict[str, str | Any]] = [
        {
            "username": "rodolfo.olivieri3@gmail.com",
            "nickname": "r0x0d",
            "provider": ProviderEnum.google,
            "secret_key": Fernet.generate_key().decode(),
        },
    ]

    def validate_seed(self, seed: dict[str, str]) -> bool:
        """Validate if a seed already exists in the database.

        :param seed: The current seed being seeded.
        """
        logger.debug(
            "Validating the current seed with username: '%s'",
            seed["username"],
        )

        result = self.repository.select_by_username(  # type: ignore
            username=seed["username"],
        )
        if result:
            logger.debug("Seed already exists in the database")
            return True

        return False

    def __init__(
        self,
        repository: type[AccountRepository] = AccountRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
