from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.account import AccountModel, ProviderEnum


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
