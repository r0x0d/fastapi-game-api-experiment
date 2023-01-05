import random
import string

import httpx
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from carnage.api.auth.authentication import generate_jwt
from carnage.api.routes.authentication.base import BaseAuthentication
from carnage.database.models.account import ProviderEnum


class GithubAuthenticationRoute(BaseAuthentication):
    def __init__(
        self,
        name: str = "github",
    ) -> None:
        """Constructor for HTTP API route.

        :param name: The name of the route
        """
        super().__init__(
            name=name,
            config={
                "api_base_url": "https://api.github.com/",
                "access_token_url": "https://github.com/login/oauth/access_token",  # noqa
                "authorize_url": "https://github.com/login/oauth/authorize",
                "client_kwargs": {"scope": "user:email"},
            },
        )

        self.router = APIRouter(
            prefix="/authentication",
            tags=["authentication"],
        )

        self.router.add_api_route(
            "/github/login",
            self.github_login,
            methods=["GET"],
            status_code=200,
        )
        self.router.add_api_route(
            "/github/auth",
            self.github_auth,
            methods=["GET"],
            status_code=200,
        )

    async def github_login(self, request: Request) -> RedirectResponse:
        """Async method that handle the initial github login page.

        :param request: The data send throught the request.
        """
        redirect_uri = request.url_for("github_auth")
        return await self.oauth.github.authorize_redirect(
            request,
            redirect_uri,
        )

    async def github_auth(self, request: Request) -> str:
        """Async method that handles the authentication for github.

        :param request: The data send throught the request.
        """
        token = await self.oauth.github.authorize_access_token(request)

        userinfo = httpx.get(
            url="https://api.github.com/user",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token['access_token']}",
            },
        ).json()

        claims = {
            "iss": "https://api.github.com/",
            "azp": "api.github.com",
            "sub": str(userinfo.get("id")),
            "email": userinfo.get("email"),
            "email_verified": False if not userinfo.get("email") else True,
            "nonce": "".join(
                random.choice(string.ascii_letters) for _ in range(10)
            ),
            "name": userinfo.get("name"),
            "preferred_username": userinfo.get("login"),
            "profile": userinfo.get("html_url"),
            "picture": userinfo.get("avatar_url"),
            "website": userinfo.get("blog"),
        }

        # The email can be be None despite the scope being 'user:email'.
        # That is because a user can choose to make his/her email private. If
        # that is the case we get all the users emails regardless if private or
        # note and use the one he/she has marked as `primary`
        if claims.get("email") is None:
            emails = httpx.get(
                url="https://api.github.com/user/emails",
                headers={
                    "Accept": "application/vnd.github+json",
                    "Authorization": f"Bearer {token['access_token']}",
                },
            ).json()
            for email in emails:
                if email["primary"]:
                    claims["email"] = email["email"]

        await self.handle_user_account(
            username=claims["email"],
            nickname=claims["preferred_username"],
            provider=ProviderEnum.github,
        )

        return generate_jwt(claims)


route = GithubAuthenticationRoute()
