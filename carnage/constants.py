"""Module to hold all global pre-defined variables."""
import os

CARNAGE_ENVIRONMENT: str | None = os.getenv(
    "CARNAGE_ENVIRONMENT",
    "development",
)
CARNAGE_SESSION_SECRET_KEY: str | None = os.getenv(
    "CARNAGE_SESSION_SECRET_KEY",
)
CARNAGE_CHAT_SECRET_KEY: str = os.getenv("CARNAGE_CHAT_SECRET_KEY", "")

DATABASE_USERNAME: str | None = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD: str | None = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST: str | None = os.getenv("DATABASE_HOST")
DATABASE_NAME: str | None = os.getenv("DATABASE_NAME")

JWT_SECRET_KEY: str | None = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM: str | None = os.getenv("JWT_ALGORITHM", "HS256")
