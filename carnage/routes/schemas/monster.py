from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster import MonsterModel

ListMonsterSchema = sqlalchemy_to_pydantic(MonsterModel)
UpdateMonsterSchema = sqlalchemy_to_pydantic(MonsterModel, config=None)
CreateMonsterSchema = sqlalchemy_to_pydantic(MonsterModel, config=None)
