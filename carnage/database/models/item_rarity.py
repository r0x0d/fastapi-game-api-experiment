from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ItemRarityModel(BaseModel):
    __tablename__ = "item_rarities"

    name = Column(String(100))
    description = Column(String())
