from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, HTTPException, Request
from starlette.config import Config
from starlette.responses import HTMLResponse, RedirectResponse

from carnage.api.auth.authentication import generate_jwt
from carnage.constants import CARNAGE_ENVIRONMENT
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
        self.account_repository = AccountRepository()
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
        if CARNAGE_ENVIRONMENT == "development":  # pragma: no cover
            self.router.add_api_route(
                "/",
                self.homepage,
                methods=["GET"],
                status_code=200,
            )

    async def google_login(self, request: Request) -> RedirectResponse:
        redirect_uri = request.url_for("google_auth")
        return await oauth.google.authorize_redirect(request, redirect_uri)

    async def google_auth(self, request: Request) -> str:
        token = await oauth.google.authorize_access_token(request)
        claims = token["userinfo"]

        user = self.account_repository.select_by_username(
            username=claims["email"],
        )
        if not user:
            raise HTTPException(
                status_code=403,
                detail="Couldn't find the user.",
            )

        return generate_jwt(claims=claims)

    # Only used or testing purposes
    if CARNAGE_ENVIRONMENT == "development":  # pragma: no cover

        async def homepage(self, request: Request) -> HTMLResponse:
            return HTMLResponse(
                """
    <li>
        <a href="/api/v1/authentication/google/login">Google Login</a>
    </li>
    """,
            )


route = AuthenticationRoute()
