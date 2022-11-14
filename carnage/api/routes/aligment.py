from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.aligment import (
    CreateAligmentSchema,
    ListAligmentSchema,
    UpdateAligmentSchema,
)
from carnage.database.repository.aligment import AligmentRepository


class AligmentRoute(BaseRoute):
    list_schema = ListAligmentSchema
    create_schema = CreateAligmentSchema
    update_schema = UpdateAligmentSchema

    def __init__(
        self,
        name: str = "aligment",
        tags: list[str] = ["aligment"],
        repository: Type[AligmentRepository] = AligmentRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListAligmentSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListAligmentSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateAligmentSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateAligmentSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = AligmentRoute()
