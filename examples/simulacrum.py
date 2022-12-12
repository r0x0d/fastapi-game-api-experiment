from carnage.database.repository.monster.monster import MonsterRepository
from carnage.monsters.dragon import Dragon

repository = MonsterRepository()

monster = repository.select_by_name(name="Dragon")
a = Dragon(monster[0])
result = a.attack(3)

print(result)
