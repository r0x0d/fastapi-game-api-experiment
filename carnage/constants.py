import os

CARNAGE_ENVIRONMENT: str = os.getenv("CARNAGE_ENVIRONMENT", "development")
CARNAGE_SECRET_KEY: str = os.getenv("CARNAGE_SECRET_KEY", "")

DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME", "")
DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
DATABASE_HOST: str = os.getenv("DATABASE_HOST", "")
DATABASE_NAME: str = os.getenv("DATABASE_NAME", "")

JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
