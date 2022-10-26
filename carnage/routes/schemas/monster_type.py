from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster_type import MonsterTypeModel

ListMonsterTypeSchema = sqlalchemy_to_pydantic(MonsterTypeModel)
UpdateMonsterTypeSchema = sqlalchemy_to_pydantic(MonsterTypeModel, config=None)
CreateMonsterTypeSchema = sqlalchemy_to_pydantic(MonsterTypeModel, config=None)
