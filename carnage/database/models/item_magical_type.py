from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ItemMagicalTypeModel(BaseModel):
    __tablename__ = "item_magical_types"

    name = Column(String(100))
    description = Column(String())
