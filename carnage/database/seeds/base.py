from typing import Any, Type

from carnage.database.repository.base import BaseRepository


class BaseSeed:
    name: str = "base"

    @property
    def data(self) -> list[dict[str, Any]]:
        pass

    def __init__(self, repository: Type[BaseRepository]) -> None:
        self.repository = repository()

    def seed(self) -> None:
        if not self.data:
            raise ValueError(f"No seed data found for {self.name}")

        print(f"Seeding {self.name}")
        self.repository.insert(self.data)
