from typing import Type

from fastapi import HTTPException, Request

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.account import ListAccountSchema, UpdateAccountSchema
from carnage.database.repository.account import AccountRepository


class AccountRoute(BaseRoute):
    list_schema = ListAccountSchema
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

    async def post(self, request: Request) -> None:
        raise HTTPException(
            status_code=418,
            detail="I can't do anything. I'm a teapot.",
        )

    async def get(self) -> list[ListAccountSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListAccountSchema:
        return await super().get_by_id(identifier)

    async def put(self, request: UpdateAccountSchema, identifier: str) -> None:
        return await super().put(request, identifier)


route = AccountRoute()
