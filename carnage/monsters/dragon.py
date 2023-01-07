from carnage.database.models.monster.monster import MonsterModel
from carnage.monsters.base import BaseMonster


class Dragon(BaseMonster):
    def __init__(self, monster: MonsterModel) -> None:
        """Class that interprets an specific monster.

        :param monster: The model that represents this monster.
        """
        super().__init__(monster)
