import json

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request
from starlette.config import Config
from starlette.responses import HTMLResponse, RedirectResponse

from carnage.constants import DEVELOPMENT
from carnage.database.repository.account import AccountRepository

router = APIRouter(prefix="/authentication", tags=["authentication"])
repository = AccountRepository()

config = Config()
oauth = OAuth(config)

oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",  # noqa
    client_kwargs={"scope": "openid email profile"},
)
oauth.register(
    name="twitter",
    api_base_url="https://api.twitter.com/1.1/",
    request_token_url="https://api.twitter.com/oauth/request_token",
    access_token_url="https://api.twitter.com/oauth/access_token",
    authorize_url="https://api.twitter.com/oauth/authenticate",
)
oauth.register(
    name="github",
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "user:email"},
)


@router.get("/google/login")
async def google_login(request: Request) -> RedirectResponse:
    redirect_uri = request.url_for("google_auth")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/auth")
async def google_auth(request: Request) -> str:
    token = await oauth.google.authorize_access_token(request)
    user = token["userinfo"]
    return user


# Only used or testing purposes
if DEVELOPMENT:  # pragma: no cover

    @router.get("/")
    async def homepage(request: Request) -> HTMLResponse:
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

    @router.get("/logout")
    async def logout(request: Request) -> RedirectResponse:
        request.session.pop("user", None)
        return RedirectResponse(url="/")
