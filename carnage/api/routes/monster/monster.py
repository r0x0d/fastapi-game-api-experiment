from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.monster import (
    CreateMonsterSchema,
    ListMonsterSchema,
    UpdateMonsterSchema,
)
from carnage.database.repository.monster import MonsterRepository


class MonsterRoute(BaseRoute):
    list_schema = ListMonsterSchema
    create_schema = CreateMonsterSchema
    update_schema = UpdateMonsterSchema

    def __init__(
        self,
        name: str = "monster",
        tags: list[str] = ["monster"],
        repository: Type[MonsterRepository] = MonsterRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListMonsterSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMonsterSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateMonsterSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateMonsterSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = MonsterRoute()
