from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemBaseTypeModel


class ListItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    pass


class UpdateItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    pass


class CreateItemBaseTypeSchema(
    sqlalchemy_to_pydantic(ItemBaseTypeModel),  # type: ignore
):
    pass
