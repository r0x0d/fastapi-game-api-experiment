"""Module that implements the Google Route."""

import random
import string
from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from carnage.api.auth.authentication import generate_jwt
from carnage.api.routes.authentication.base import BaseAuthentication
from carnage.database.models.account import ProviderEnum


class GoogleAuthenticationRoute(BaseAuthentication):
    """Class that overrides the base routes for an API request."""

    def __init__(
        self,
        name: str = "google",
        config: dict[str, Any] = {},
    ) -> None:
        """Constructor for HTTP API route.

        :param name: The name of the route
        """
        super().__init__(
            name=name,
            config=config
            or {
                "api_base_url": "https://www.googleapis.com/",
                "server_metadata_url": "https://accounts.google.com/.well-known/openid-configuration",  # noqa
                "client_kwargs": {"scope": "openid email profile"},
            },
        )

        self.router = APIRouter(
            prefix="/authentication",
            tags=["authentication"],
        )

        self.router.add_api_route(
            "/google/login",
            self.google_login,
            methods=["GET"],
            status_code=200,
        )
        self.router.add_api_route(
            "/google/auth",
            self.google_auth,
            methods=["GET"],
            status_code=200,
        )

    async def google_login(self, request: Request) -> RedirectResponse:
        """Async method that handle the initial gitlab login page.

        :param request: The data send throught the request.
        """
        redirect_uri = request.url_for("google_auth")
        return await self.oauth.google.authorize_redirect(
            request,
            redirect_uri,
        )

    async def google_auth(self, request: Request) -> str:
        """Async method that handles the authentication for google.

        :param request: The data send throught the request.
        """
        token = await self.oauth.google.authorize_access_token(request)
        claims = token["userinfo"]

        await self.handle_user_account(
            username=claims["email"],
            nickname="".join(
                random.choice(string.ascii_letters) for _ in range(10)
            ),
            provider=ProviderEnum.google,
        )

        return generate_jwt(claims)


route = GoogleAuthenticationRoute()
