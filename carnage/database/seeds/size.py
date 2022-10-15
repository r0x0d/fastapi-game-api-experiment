from typing import Any, Type

from carnage.database.repository.size import SizeRepository
from carnage.database.seeds.base import BaseSeed


class SizeSeed(BaseSeed):
    name: str = "size"
    data: list[dict[str, Any]] = [
        {
            "name": "Small",
        },
        {
            "name": "Medium",
        },
        {
            "name": "Big",
        },
    ]

    def __init__(
        self,
        repository: Type[SizeRepository] = SizeRepository,
    ) -> None:
        super().__init__(repository=repository)
