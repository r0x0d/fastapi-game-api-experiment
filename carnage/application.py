from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from carnage.constants import DEVELOPMENT
from carnage.database.repository.setting import SettingRepository
from carnage.routes.account import account_route
from carnage.routes.aligment import aligment_route
from carnage.routes.authentication import authentication_route
from carnage.routes.item import item_route
from carnage.routes.item_base_type import item_base_type_route
from carnage.routes.item_magical_type import item_magical_type_route
from carnage.routes.item_rarity import item_rarity_route
from carnage.routes.monster import monster_route
from carnage.routes.monster_type import monster_type_route
from carnage.routes.race import race_route
from carnage.routes.size import size_route
from carnage.routes.spell import spell_route
from carnage.routes.spell_duration_type import spell_duration_type_route
from carnage.routes.spell_range_type import spell_range_type_route
from carnage.routes.spell_school import spell_school_route


def add_router(app: FastAPI) -> None:
    [
        app.include_router(router=router, prefix="/api/v1")
        for router in [
            account_route.router,
            aligment_route.router,
            authentication_route.router,
            item_base_type_route.router,
            item_magical_type_route.router,
            item_rarity_route.router,
            item_route.router,
            monster_route.router,
            monster_type_route.router,
            size_route.router,
            spell_duration_type_route.router,
            spell_range_type_route.router,
            spell_route.router,
            spell_school_route.router,
            race_route.router,
        ]
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

    add_router(app)
    add_middleware(app)

    return app
