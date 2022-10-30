from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster import MonsterModel
from carnage.database.repository.monster import MonsterRepository
from carnage.routes.base import BaseRoute

ListMonsterSchema = sqlalchemy_to_pydantic(MonsterModel)
UpdateMonsterSchema = sqlalchemy_to_pydantic(MonsterModel, config=None)
CreateMonsterSchema = sqlalchemy_to_pydantic(MonsterModel, config=None)


class MonsterRoute(BaseRoute):
    def __init__(
        self,
        name: str = "monster",
        tags: list[str] = ["monster"],
        repository: Type[MonsterRepository] = MonsterRepository,
        get_response_model: BaseModel = ListMonsterSchema,
        post_response_model: BaseModel = CreateMonsterSchema,
        put_response_model: BaseModel = UpdateMonsterSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = MonsterRoute()
