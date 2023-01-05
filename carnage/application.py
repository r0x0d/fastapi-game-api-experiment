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
    chat,
    condition,
    debug,
    difficulty,
    dungeon,
    game_mode,
    item,
    monster,
    player,
    race,
    size,
    spell,
    vocation,
)
from carnage.constants import CARNAGE_ENVIRONMENT, CARNAGE_SESSION_SECRET_KEY


def add_router(app: FastAPI) -> None:
    """Add routes to the main instance of FastAPI.

    :param app: The FastAPI instance used.
    """
    [
        app.include_router(router=router, prefix="/api/v1")
        for router in [
            account.route.router,
            aligment.route.router,
            authentication.github.route.router,
            authentication.gitlab.route.router,
            authentication.google.route.router,
            chat.channel_chat.route.router,
            chat.global_chat.route.router,
            condition.route.router,
            dungeon.dungeon.route.router,
            dungeon.dungeon_difficulty.route.router,
            dungeon.dungeon_schema.route.router,
            difficulty.route.router,
            game_mode.route.router,
            item.item.route.router,
            item.item_base_type.route.router,
            item.item_magical_type.route.router,
            item.item_rarity.route.router,
            monster.monster.route.router,
            monster.monster_type.route.router,
            player.route.router,
            race.route.router,
            size.route.router,
            spell.spell.route.router,
            spell.spell_duration_type.route.router,
            spell.spell_range_type.route.router,
            spell.spell_school.route.router,
            vocation.vocation.route.router,
            vocation.vocation_spell.route.router,
        ]
    ]

    # Only used during development
    if CARNAGE_ENVIRONMENT == "development":
        app.include_router(router=debug.route.router)


def add_middleware(app: FastAPI) -> None:
    """Add FastAPI middlewares to the main application.

    :param app: The FastAPI instance used.
    """
    app.add_middleware(
        SessionMiddleware,
        secret_key=CARNAGE_SESSION_SECRET_KEY,
    )
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
    """Create the initial FastAPI application."""
    app = FastAPI()

    add_router(app)
    add_middleware(app)

    return app
