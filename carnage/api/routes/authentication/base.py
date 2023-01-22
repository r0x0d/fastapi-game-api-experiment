# MIT License
#
# Copyright (c) 2022, Rodolfo Olivieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
