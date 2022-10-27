from typing import Type

from carnage.database.repository.account import AccountRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.account import (
    CreateAccountSchema,
    ListAccountSchema,
    UpdateAccountSchema,
)


class AccountRoute(BaseRoute):
    def __init__(
        self,
        name: str = "account",
        tags: list[str] = ["account"],
        repository: Type[AccountRepository] = AccountRepository,
        get_response_model: Type[ListAccountSchema] = ListAccountSchema,
        post_response_model: Type[CreateAccountSchema] = CreateAccountSchema,
        put_response_model: Type[UpdateAccountSchema] = UpdateAccountSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


account_route = AccountRoute()
