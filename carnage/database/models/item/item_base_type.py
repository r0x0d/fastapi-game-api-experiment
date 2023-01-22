"""Module that represents the Item Base Type Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ItemBaseTypeModel(BaseModel):
    """A model-class that represents an Item Base Type."""

    __tablename__ = "item_base_types"

    name = Column(String(100))
    description = Column(String())
