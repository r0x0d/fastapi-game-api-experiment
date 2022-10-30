from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster.monster_type import MonsterTypeModel
from carnage.database.repository.monster.monster_type import (
    MonsterTypeRepository,
)
from carnage.routes.base import BaseRoute

ListMonsterTypeSchema = sqlalchemy_to_pydantic(MonsterTypeModel)
UpdateMonsterTypeSchema = sqlalchemy_to_pydantic(MonsterTypeModel, config=None)
CreateMonsterTypeSchema = sqlalchemy_to_pydantic(MonsterTypeModel, config=None)


class MonsterTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "monster_type",
        tags: list[str] = ["monster", "monster_type"],
        repository: Type[MonsterTypeRepository] = MonsterTypeRepository,
        get_response_model: BaseModel = ListMonsterTypeSchema,
        post_response_model: BaseModel = CreateMonsterTypeSchema,
        put_response_model: BaseModel = UpdateMonsterTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = MonsterTypeRoute()
