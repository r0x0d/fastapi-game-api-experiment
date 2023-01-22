"""Module that represents the Condition seeding."""

from carnage.database.repository.condition import ConditionRepository
from carnage.database.seeds.base import BaseSeed


class ConditionSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "condition"
    data: list[dict[str, str | bool]] = [
        {
            "name": "Blind",
            "description": "Apply blind.",
            "is_permanent": False,
        },
        {
            "name": "Permanent Slow",
            "description": "Apply a permanent slow",
            "is_permanent": True,
        },
    ]

    def __init__(
        self,
        repository: type[ConditionRepository] = ConditionRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
