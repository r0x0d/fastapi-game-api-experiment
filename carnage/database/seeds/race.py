from typing import Any, Type

from carnage.database.repository.aligment import AligmentRepository
from carnage.database.repository.race import RaceRepository
from carnage.database.repository.size import SizeRepository
from carnage.database.seeds.base import BaseSeed


class RaceSeed(BaseSeed):
    name: str = "race"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
        },
    ]

    def __init__(
        self,
        repository: Type[RaceRepository] = RaceRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.size_repository = SizeRepository()
        self.aligment_repository = AligmentRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
        aligment = self.aligment_repository.select_first()
        size = self.size_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "aligment_id": aligment[0].id,
                    "size_id": size[0].id,
                },
            )

        super().seed()
