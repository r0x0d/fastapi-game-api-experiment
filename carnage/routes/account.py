from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.account import AccountModel
from carnage.database.models.base import BaseModel
from carnage.database.repository.account import AccountRepository
from carnage.routes.base import BaseRoute

ListAccountSchema = sqlalchemy_to_pydantic(
    AccountModel,
    exclude=("password", "secret_key"),
)
UpdateAccountSchema = sqlalchemy_to_pydantic(
    AccountModel,
    config=None,
    exclude=("provider", "secret_key"),
)
CreateAccountSchema = sqlalchemy_to_pydantic(
    AccountModel,
    config=None,
    exclude=("secret_key"),
)
CreateAccountSchema.provider = "carnage"


class AccountRoute(BaseRoute):
    def __init__(
        self,
        name: str = "account",
        tags: list[str] = ["account"],
        repository: Type[AccountRepository] = AccountRepository,
        get_response_model: BaseModel = ListAccountSchema,
        post_response_model: BaseModel = CreateAccountSchema,
        put_response_model: BaseModel = UpdateAccountSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = AccountRoute()
