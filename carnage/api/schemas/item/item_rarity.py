from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemRarityModel


class ListItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    pass


class UpdateItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    pass


class CreateItemRaritySchema(
    sqlalchemy_to_pydantic(ItemRarityModel),  # type: ignore
):
    pass
