from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.aligment import AligmentModel


class ListAligmentSchema(
    sqlalchemy_to_pydantic(AligmentModel),  # type: ignore
):
    pass


class UpdateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    pass


class CreateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    pass
