from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster.monster_type import MonsterTypeModel


class ListMonsterTypeSchema(
    sqlalchemy_to_pydantic(MonsterTypeModel),  # type: ignore
):
    pass


class UpdateMonsterTypeSchema(
    sqlalchemy_to_pydantic(MonsterTypeModel, config=None),  # type: ignore
):
    pass


class CreateMonsterTypeSchema(
    sqlalchemy_to_pydantic(MonsterTypeModel, config=None),  # type: ignore
):
    pass
