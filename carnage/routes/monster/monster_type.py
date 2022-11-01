from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.monster.monster_type import MonsterTypeModel
from carnage.database.repository.monster.monster_type import (
    MonsterTypeRepository,
)
from carnage.routes.base import BaseRoute


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
