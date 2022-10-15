import os

if os.getenv("DEVELOPMENT", False):
    from dotenv import load_dotenv

    load_dotenv()

DATABASE_USERNAME: str = os.getenv("DATABASE_USERNAME", "")
DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
DATABASE_HOST: str = os.getenv("DATABASE_HOST", "")
DATABASE_NAME: str = os.getenv("DATABASE_NAME", "")
