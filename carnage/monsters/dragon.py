"""Module that is a representation of a monster, a  Dragon."""

from carnage.database.models.monster import MonsterModel
from carnage.monsters.base import BaseMonster


class Dragon(BaseMonster):
    """Class that override the methods and properties of a monster."""

    def __init__(self, monster: MonsterModel) -> None:
        """Class that interprets an specific monster.

        :param monster: The model that represents this monster.
        """
        super().__init__(monster)
