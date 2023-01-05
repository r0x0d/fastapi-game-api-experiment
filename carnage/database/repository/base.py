from datetime import datetime
from functools import lru_cache
from typing import Any

from sqlalchemy import insert, select, update

from carnage.database.models.base import BaseModel
from carnage.database.session import session


class BaseRepository:
    def __init__(self, model: BaseModel = BaseModel) -> None:
        """Default constructor for base repository.

        :param model: The model used in the repository.
        """
        self.session = session
        self.model = model

    def insert(self, values: list[dict[str, Any]] | dict[str, Any]) -> None:
        """Default method to make insertions in the database.

        :param values: List or dictionary of values to insert
        """
        statement = insert(self.model).values(values)

        with self.session() as session:
            session.execute(statement=statement)
            session.commit()

    @lru_cache
    def select(self) -> list[BaseModel]:
        """Default method to retrieve information from the database."""
        statement = select(self.model).where(
            self.model.deleted_at == None,  # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).scalars().all()

    @lru_cache
    def select_first(self) -> BaseModel:
        """Default method to get first information from the database."""
        statement = select(self.model).where(
            self.model.deleted_at == None,  # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()

    @lru_cache
    def select_by_id(self, identifier: str) -> BaseModel:
        """Default method to select by filtering using an identifier.

        :param identifier: The unique identifier to query in the database.
        """
        statement = select(self.model).where(
            self.model.id == identifier
            and self.model.deleted_at == None,  # noqa
        )
        with self.session() as session:
            return session.execute(statement=statement).first()

    @lru_cache
    def select_by_name(self, name: str) -> BaseModel:
        """Default method to select rows by using a name.

        :param name: The name to use in the query in the database.
        """
        statement = select(self.model).where(
            self.model.name == name and self.model.deleted_at == None,  # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()

    def update(self, values: dict[str, Any], identifier: str) -> None:
        """Default method to update values in the database.

        :param values: Dictionary of values to update in the database.
        :param identifier: The unique identifier to query in the database.
        """
        statement = (
            update(self.model)
            .values(values)
            .where(
                self.model.id == identifier,
            )
        )

        with self.session() as session:
            session.execute(statement=statement)
            session.commit()

    def delete(self, identifier: str) -> None:
        """Default method to remove entries from the database.

        This method will actually call `update` internally to update the
        `deleted_at` field in the table.

        :param identifier: The unique identifier to query in the database.
        """
        statement = (
            update(self.model)
            .values({"deleted_at": datetime.now()})
            .where(self.model.id == identifier)
        )

        with self.session() as session:
            session.execute(statement=statement)
            session.commit()
