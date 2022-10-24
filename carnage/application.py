from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from carnage.constants import DEVELOPMENT
from carnage.database.repository.setting import SettingRepository
from carnage.routes import (
    account,
    aligment,
    authentication,
    monster,
    monster_type,
    size,
)


def add_middleware(app: FastAPI) -> None:
    setting_repository = SettingRepository()

    result = setting_repository.select_by_environment()
    app.add_middleware(SessionMiddleware, secret_key=result[0].secret_key)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    if not DEVELOPMENT:
        app.add_middleware(HTTPSRedirectMiddleware)
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["carnage.io", "*.carnage.io"],
        )


def create_app() -> FastAPI:
    """."""
    app = FastAPI()

    app.include_router(aligment.router)
    app.include_router(monster.router)
    app.include_router(monster_type.router)
    app.include_router(size.router)
    app.include_router(account.router)
    app.include_router(authentication.router)

    add_middleware(app)

    return app
