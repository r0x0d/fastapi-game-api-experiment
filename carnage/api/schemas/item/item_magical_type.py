from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemMagicalTypeModel


class ListItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    pass


class UpdateItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    pass


class CreateItemMagicalTypeSchema(
    sqlalchemy_to_pydantic(ItemMagicalTypeModel),  # type: ignore
):
    pass
