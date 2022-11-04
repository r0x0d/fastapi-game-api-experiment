from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.size import SizeModel


class ListSizeSchema(
    sqlalchemy_to_pydantic(SizeModel),  # type: ignore
):
    pass


class UpdateSizeSchema(
    sqlalchemy_to_pydantic(SizeModel, config=None),  # type: ignore
):
    pass


class CreateSizeSchema(
    sqlalchemy_to_pydantic(SizeModel, config=None),  # type: ignore
):
    pass
