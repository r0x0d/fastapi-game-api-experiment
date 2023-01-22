"""Module that implements the Base Authentication Route."""

import logging
from typing import Any

from authlib.integrations.starlette_client import OAuth
from cryptography.fernet import Fernet
from starlette.config import Config

from carnage.database.models.account import ProviderEnum
from carnage.database.repository.account import AccountRepository

logger = logging.getLogger(__name__)


class BaseAuthentication:
    """Class that implements the base routes for an API request."""

    def __init__(self, name: str, config: dict[str, Any] = {}) -> None:
        """Base constructor for all authentication API routes.

        :param name: The name of the route.
        :param config: The configuration that is used under oauthlib.
        """
        self.name = name
        self.oauth = OAuth(Config())
        self.config = config
        self.account_repository = AccountRepository()

        self.register()

    def register(self) -> None:
        """Register the social login method requested."""
        logger.info("Registering social '%s'", (self.name))
        self.oauth.register(name=self.name, **self.config)

    async def handle_user_account(
        self,
        username: str,
        nickname: str,
        provider: ProviderEnum,
    ) -> None:
        """Handle the user information in the database.

        This method will try to create a new account if needed, otherwise, will
        not do anything as the account is already present.

        :param username: The username for the account.
        :param nickname: The nickname for the account.
        :param provider: The provider tied to the account.
        """
        account = self.account_repository.select_by_username(
            username=username,
        )

        if not account:
            logger.info("Account does not exist. Creating a new one.")

            self.account_repository.insert(
                {
                    "username": username,
                    "nickname": nickname,
                    "provider": provider,
                    "secret_key": Fernet.generate_key().decode(),
                },
            )
