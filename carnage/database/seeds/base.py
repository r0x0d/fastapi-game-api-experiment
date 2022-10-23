from typing import Any, Type

from carnage.database.repository.base import BaseRepository


class BaseSeed:
    name: str = "base"
    data: list[dict[str, Any]] = [{}]

    def __init__(
        self,
        repository: Type[BaseRepository] = BaseRepository,
    ) -> None:
        self.repository = repository()

    def seed(self) -> None:
        if not self.data:
            raise ValueError(f"No seed data found for {self.name}")

        self.repository.insert(self.data)
        print(f"Seeded {self.name}")
