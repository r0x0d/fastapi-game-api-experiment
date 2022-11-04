from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.monster import (
    CreateMonsterTypeSchema,
    ListMonsterTypeSchema,
    UpdateMonsterTypeSchema,
)
from carnage.database.repository.monster.monster_type import (
    MonsterTypeRepository,
)


class MonsterTypeRoute(BaseRoute):
    list_schema = ListMonsterTypeSchema
    create_schema = CreateMonsterTypeSchema
    update_schema = UpdateMonsterTypeSchema

    def __init__(
        self,
        name: str = "monster_type",
        tags: list[str] = ["monster", "monster_type"],
        repository: Type[MonsterTypeRepository] = MonsterTypeRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListMonsterTypeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMonsterTypeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateMonsterTypeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateMonsterTypeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = MonsterTypeRoute()
