"""Module that represents the Monster Type seeding."""

from typing import Any

from carnage.database.repository.monster import MonsterTypeRepository
from carnage.database.seeds.base import BaseSeed


class MonsterTypeSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "monster_type"
    data: list[dict[str, Any]] = [
        {
            "name": "Dragon",
        },
        {
            "name": "Kobold",
        },
        {
            "name": "Undead",
        },
    ]

    def __init__(
        self,
        repository: type[MonsterTypeRepository] = MonsterTypeRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
