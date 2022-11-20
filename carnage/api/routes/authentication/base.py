import logging
from typing import Any

from authlib.integrations.starlette_client import OAuth
from cryptography.fernet import Fernet
from starlette.config import Config

from carnage.database.models.account import ProviderEnum
from carnage.database.repository.account import AccountRepository

logger = logging.getLogger(__name__)


class BaseAuthentication:
    def __init__(self, name: str, config: dict[str, Any] = {}) -> None:
        self.name = name
        self.oauth = OAuth(Config())
        self.config = config
        self.account_repository = AccountRepository()

        self.register()

    def register(self) -> None:
        logger.info("Registering social '%s'", (self.name))
        self.oauth.register(name=self.name, **self.config)

    async def handle_user_account(
        self,
        username: str,
        provider: ProviderEnum,
    ) -> None:
        account = self.account_repository.select_by_username(
            username=username,
        )

        if not account:
            logger.info("Account does not exist. Creating a new one.")

            self.account_repository.insert(
                {
                    "username": username,
                    "nickname": "something",
                    "provider": provider,
                    "secret_key": Fernet.generate_key(),
                },
            )
