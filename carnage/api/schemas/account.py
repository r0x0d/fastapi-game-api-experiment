"""Module to represent an Account schema."""
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.account import AccountModel


class ListAccountSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AccountModel,
        exclude=("password", "secret_key"),
    ),
):
    """Class that represents a listing of elements."""


class UpdateAccountSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AccountModel,
        config=None,
        exclude=("provider", "secret_key"),
    ),
):
    """Class that represents an update of elements."""
