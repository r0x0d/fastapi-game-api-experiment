from fastapi import FastAPI

from carnage.routes import aligment, monster, monster_type, size


def create_app() -> FastAPI:
    """."""
    app = FastAPI()

    app.include_router(aligment.router)
    app.include_router(monster.router)
    app.include_router(monster_type.router)
    app.include_router(size.router)
    return app
