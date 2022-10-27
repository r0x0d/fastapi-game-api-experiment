from typing import Type

from carnage.database.repository.monster import MonsterRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.monster import (
    CreateMonsterSchema,
    ListMonsterSchema,
    UpdateMonsterSchema,
)


class MonsterRoute(BaseRoute):
    def __init__(
        self,
        name: str = "monster",
        tags: list[str] = ["monster"],
        repository: Type[MonsterRepository] = MonsterRepository,
        get_response_model: Type[ListMonsterSchema] = ListMonsterSchema,
        post_response_model: Type[CreateMonsterSchema] = CreateMonsterSchema,
        put_response_model: Type[UpdateMonsterSchema] = UpdateMonsterSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


monster_route = MonsterRoute()
