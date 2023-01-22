"""Module that represents the Aligment Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class AligmentModel(BaseModel):
    """A model-class that represents an Aligment."""

    __tablename__ = "aligments"

    name = Column(String(100))
