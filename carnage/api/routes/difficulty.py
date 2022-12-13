from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.difficulty import (
    CreateDifficultySchema,
    ListDifficultySchema,
    UpdateDifficultySchema,
)
from carnage.database.repository.difficulty import DifficultyRepository


class DifficultyRoute(BaseRoute):
    list_schema = ListDifficultySchema
    update_schema = CreateDifficultySchema
    create_schema = UpdateDifficultySchema

    def __init__(
        self,
        name: str = "difficulty",
        tags: list[str] = ["difficulty"],
        repository: Type[DifficultyRepository] = DifficultyRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListDifficultySchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListDifficultySchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateDifficultySchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateDifficultySchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = DifficultyRoute()
