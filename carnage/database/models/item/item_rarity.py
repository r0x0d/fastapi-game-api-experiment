"""Module that represents the Item Rarity Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ItemRarityModel(BaseModel):
    """A model-class that represents an Item Rarity."""

    __tablename__ = "item_rarities"

    name = Column(String(100))
    description = Column(String())
