from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from carnage.constants import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_USERNAME,
)


def create_session() -> sessionmaker:
    """Create a new database session.

    :return: A new database session.
    :rtype: sessionmaker.
    """
    engine = create_engine(
        f"postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}",  # noqa
    )
    return sessionmaker(bind=engine)


#: Global instance of a session for sqlalchemy.
session = create_session()
