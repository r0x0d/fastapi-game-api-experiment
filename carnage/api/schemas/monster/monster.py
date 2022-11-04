from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster import MonsterModel


class ListMonsterSchema(
    sqlalchemy_to_pydantic(MonsterModel),  # type: ignore
):
    pass


class UpdateMonsterSchema(
    sqlalchemy_to_pydantic(MonsterModel, config=None),  # type: ignore
):
    pass


class CreateMonsterSchema(
    sqlalchemy_to_pydantic(MonsterModel, config=None),  # type: ignore
):
    pass
