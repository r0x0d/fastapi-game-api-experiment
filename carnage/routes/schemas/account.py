from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.account import AccountModel

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
