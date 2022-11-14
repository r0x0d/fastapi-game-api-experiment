from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.account import (
    CreateAccountSchema,
    ListAccountSchema,
    UpdateAccountSchema,
)
from carnage.database.repository.account import AccountRepository


class AccountRoute(BaseRoute):
    list_schema = ListAccountSchema
    create_schema = CreateAccountSchema
    update_schema = UpdateAccountSchema

    def __init__(
        self,
        name: str = "account",
        tags: list[str] = ["account"],
        repository: Type[AccountRepository] = AccountRepository,
    ) -> None:
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def get(self) -> list[ListAccountSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListAccountSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateAccountSchema) -> None:
        return await super().post(request)

    async def put(self, request: UpdateAccountSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = AccountRoute()
