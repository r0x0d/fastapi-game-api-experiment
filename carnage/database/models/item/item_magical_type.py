"""Module that represents the Item Magical Type Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ItemMagicalTypeModel(BaseModel):
    """A model-class that represents an Item Magical Type."""

    __tablename__ = "item_magical_types"

    name = Column(String(100))
    description = Column(String())
