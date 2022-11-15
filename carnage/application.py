from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from carnage.api.routes import (
    account,
    aligment,
    authentication,
    dungeon,
    item,
    monster,
    player,
    race,
    size,
    spell,
    vocation,
)
from carnage.constants import CARNAGE_ENVIRONMENT, CARNAGE_SECRET_KEY


def add_router(app: FastAPI) -> None:
    [
        app.include_router(router=router, prefix="/api/v1")
        for router in [
            account.route.router,
            aligment.route.router,
            authentication.route.router,
            player.route.router,
            race.route.router,
            size.route.router,
            item.item_base_type.route.router,
            item.item_magical_type.route.router,
            item.item_rarity.route.router,
            item.item.route.router,
            monster.monster.route.router,
            monster.monster_type.route.router,
            spell.spell_duration_type.route.router,
            spell.spell_range_type.route.router,
            spell.spell.route.router,
            spell.spell_school.route.router,
            vocation.vocation.route.router,
            vocation.vocation_spell.route.router,
            dungeon.dungeon.route.router,
            dungeon.dungeon_schema.route.router,
            dungeon.dungeon_difficulty.route.router,
        ]
    ]


def add_middleware(app: FastAPI) -> None:
    app.add_middleware(SessionMiddleware, secret_key=CARNAGE_SECRET_KEY)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "*",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if CARNAGE_ENVIRONMENT == "production":
        app.add_middleware(HTTPSRedirectMiddleware)
        app.add_middleware(
            TrustedHostMiddleware,
            allowed_hosts=["carnage.world", "*.carnage.world"],
        )


def create_app() -> FastAPI:
    """."""
    app = FastAPI()

    add_router(app)
    add_middleware(app)

    return app
