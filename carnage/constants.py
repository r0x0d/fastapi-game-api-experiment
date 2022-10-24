import os

DEVELOPMENT: str = os.getenv("DEVELOPMENT", "")

if DEVELOPMENT:  # pragma: no cover
    from dotenv import load_dotenv

    load_dotenv()

# pragma: cover
DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME", "")
DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
DATABASE_HOST: str = os.getenv("DATABASE_HOST", "")
DATABASE_NAME: str = os.getenv("DATABASE_NAME", "")
