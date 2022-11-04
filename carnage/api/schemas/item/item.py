from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemModel


class ListItemSchema(
    sqlalchemy_to_pydantic(ItemModel),  # type: ignore
):
    pass


class UpdateItemSchema(
    sqlalchemy_to_pydantic(ItemModel, config=None),  # type: ignore
):
    pass


class CreateItemSchema(
    sqlalchemy_to_pydantic(ItemModel, config=None),  # type: ignore
):
    pass
