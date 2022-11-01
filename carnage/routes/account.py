from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.account import AccountModel, ProviderEnum
from carnage.database.repository.account import AccountRepository
from carnage.routes.base import BaseRoute


class ListAccountSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AccountModel,
        exclude=("password", "secret_key"),
    ),
):
    pass


class UpdateAccountSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AccountModel,
        config=None,
        exclude=("provider", "secret_key"),
    ),
):
    pass


class CreateAccountSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AccountModel,
        config=None,
        exclude=("secret_key"),
    ),
):
    provider = ProviderEnum.carnage


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
            name,
            tags,
            repository,
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
