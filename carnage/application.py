from fastapi import APIRouter, FastAPI
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
    spell,
    spell_duration_type,
    spell_range_type,
    spell_school,
)

APPLICATION_ROUTERS: list[APIRouter] = [
    aligment.router,
    monster.router,
    monster_type.router,
    size.router,
    account.router,
    authentication.router,
    spell_school.router,
    spell_duration_type.router,
    spell_range_type.router,
    spell.router,
]


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

    [app.include_router(router) for router in APPLICATION_ROUTERS]

    add_middleware(app)

    return app
