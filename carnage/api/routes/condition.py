from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.condition import (
    CreateConditionSchema,
    ListConditionSchema,
    UpdateConditionSchema,
)
from carnage.database.repository.condition import ConditionRepository


class ConditionRoute(BaseRoute):
    list_schema = ListConditionSchema
    create_schema = CreateConditionSchema
    update_schema = UpdateConditionSchema

    def __init__(
        self,
        name: str = "condition",
        tags: list[str] = ["condition"],
        repository: Type[ConditionRepository] = ConditionRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListConditionSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListConditionSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateConditionSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateConditionSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = ConditionRoute()
