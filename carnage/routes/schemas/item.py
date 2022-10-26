from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.item import ItemModel

ListItemSchema = sqlalchemy_to_pydantic(ItemModel)
UpdateItemSchema = sqlalchemy_to_pydantic(ItemModel, config=None)
CreateItemSchema = sqlalchemy_to_pydantic(ItemModel, config=None)
