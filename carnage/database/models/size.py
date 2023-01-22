"""Module that represents the Size Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SizeModel(BaseModel):
    """A model-class that represents an Size."""

    __tablename__ = "sizes"

    name = Column(String(100))
