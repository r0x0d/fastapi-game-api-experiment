from typing import Any, Type

from carnage.database.repository.difficulty import DifficultyRepository
from carnage.database.seeds.base import BaseSeed


class DifficultySeed(BaseSeed):
    name: str = "difficulty"
    data: list[dict[str, Any]] = [
        {
            "name": "Easy",
            "description": "Easiest difficulty",
        },
    ]

    def __init__(
        self,
        repository: Type[DifficultyRepository] = DifficultyRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
