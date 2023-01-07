from functools import cached_property
from typing import Any

from carnage.monsters.base import BaseMonster
from carnage.monsters.dragon import Dragon


class MonsterManager:
    @cached_property
    def _monster_mapping(self) -> dict[str, Any]:
        """Method that maps the available monsters to their simplified name.

        :return: A dictionary with the seed name as key and a seed class
        instance as value.
        """
        # TODO(r0x0d): Change type annotation for this property in the future
        # for `BaseMonster`
        return {"dragon": Dragon}

    def select(self, monster: str) -> BaseMonster | None:
        """Select an monster out of the list of available ones and return it.

        :param monster: The name of the monster to be selected.
        """
        selected_monster = self._monster_mapping.get(monster)
        return selected_monster
