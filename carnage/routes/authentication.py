import json

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request
from starlette.config import Config
from starlette.responses import HTMLResponse, RedirectResponse

from carnage.constants import DEVELOPMENT
from carnage.database.repository.account import AccountRepository

config = Config()
oauth = OAuth(config)

oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",  # noqa
    client_kwargs={"scope": "openid email profile"},
)


class AuthenticationRoute:
    def __init__(
        self,
    ) -> None:
        self.repository = AccountRepository()
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
        self.router.add_api_route(
            "/",
            self.homepage,
            methods=["GET"],
            status_code=200,
        )
        self.router.add_api_route(
            "/logout",
            self.logout,
            methods=["GET"],
            status_code=200,
        )

    async def google_login(self, request: Request) -> RedirectResponse:
        redirect_uri = request.url_for("google_auth")
        return await oauth.google.authorize_redirect(request, redirect_uri)

    async def google_auth(self, request: Request) -> str:
        token = await oauth.google.authorize_access_token(request)
        user = token["userinfo"]
        return user

    # Only used or testing purposes
    if DEVELOPMENT:  # pragma: no cover

        async def homepage(self, request: Request) -> HTMLResponse:
            user = request.session.get("user")
            if user:
                data = json.dumps(user)
                html = f"<pre>{data}</pre>" '<a href="/logout">logout</a>'
                return HTMLResponse(html)
            return HTMLResponse(
                """
    <li>
        <a href="/authentication/google/login">Google Login</a>
    </li>
    """,
            )

        async def logout(self, request: Request) -> RedirectResponse:
            request.session.pop("user", None)
            return RedirectResponse(url="/")


authentication_route = AuthenticationRoute()
