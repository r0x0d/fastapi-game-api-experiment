from typing import Type

from carnage.database.repository.monster_type import MonsterTypeRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.monster_type import (
    CreateMonsterTypeSchema,
    ListMonsterTypeSchema,
    UpdateMonsterTypeSchema,
)


class MonsterTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "monster_type",
        tags: list[str] = ["monster", "monster_type"],
        repository: Type[MonsterTypeRepository] = MonsterTypeRepository,
        get_response_model: Type[
            ListMonsterTypeSchema
        ] = ListMonsterTypeSchema,
        post_response_model: Type[
            CreateMonsterTypeSchema
        ] = CreateMonsterTypeSchema,
        put_response_model: Type[
            UpdateMonsterTypeSchema
        ] = UpdateMonsterTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


monster_type_route = MonsterTypeRoute()
