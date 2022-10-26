from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ItemBaseTypeModel(BaseModel):
    __tablename__ = "item_base_types"

    name = Column(String(100))
    description = Column(String())
