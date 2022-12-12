from carnage.database.models.monster.monster import MonsterModel
from carnage.monsters.base import BaseMonster


class Dragon(BaseMonster):
    def __init__(self, monster: MonsterModel) -> None:
        super().__init__(monster)
