from typing import Type

from carnage.database.repository.aligment import AligmentRepository
from carnage.database.seeds.base import BaseSeed


class AligmentSeed(BaseSeed):
    name: str = "aligment"
    data: list[dict[str, str]] = [
        {
            "name": "Good",
        },
        {
            "name": "Evil",
        },
        {
            "name": "Chaotic",
        },
    ]

    def __init__(
        self,
        repository: Type[AligmentRepository] = AligmentRepository,
    ) -> None:
        super().__init__(repository=repository)
