"""Module that represents the Spell Range Type seeding."""

from carnage.database.repository.spell import SpellRangeTypeRepository
from carnage.database.seeds.base import BaseSeed


class SpellRangeTypeSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "spell-range-type"
    data: list[dict[str, str]] = [
        {
            "name": "Self",
            "description": "Self range",
        },
        {
            "name": "Touch",
            "description": "Touch range",
        },
        {
            "name": "Ranged",
            "description": "Ranged range",
        },
        {
            "name": "Sight",
            "description": "Sight range",
        },
        {
            "name": "Unlimited",
            "description": "Unlimited range",
        },
    ]

    def __init__(
        self,
        repository: type[SpellRangeTypeRepository] = SpellRangeTypeRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
