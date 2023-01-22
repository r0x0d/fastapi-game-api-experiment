"""Module that represents the Spell School seeding."""

from carnage.database.repository.spell import SpellSchoolRepository
from carnage.database.seeds.base import BaseSeed


class SpellSchoolSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "spell-school"
    data: list[dict[str, str]] = [
        {"name": "Abjuration", "description": "Abjuration Spell"},
        {"name": "Conjuration", "description": "Conjuration Spell"},
        {"name": "Divination", "description": "Divination Spell"},
        {"name": "Enchantment", "description": "Enchantment Spell"},
        {"name": "Evocation", "description": "Evocation Spell"},
        {"name": "Illusion", "description": "Illusion Spell"},
    ]

    def __init__(
        self,
        repository: type[SpellSchoolRepository] = SpellSchoolRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
