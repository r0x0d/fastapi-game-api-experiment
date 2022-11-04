from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationModel


class ListVocationSchema(
    sqlalchemy_to_pydantic(VocationModel),  # type: ignore
):
    pass


class UpdateVocationSchema(
    sqlalchemy_to_pydantic(VocationModel, config=None),  # type: ignore
):
    pass


class CreateVocationSchema(
    sqlalchemy_to_pydantic(VocationModel, config=None),  # type: ignore
):
    pass
