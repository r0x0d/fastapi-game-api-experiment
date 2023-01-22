"""Module that represents the Difficulty Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class DifficultyModel(BaseModel):
    """A model-class that represents an Difficulty."""

    __tablename__ = "difficulties"

    name = Column(String(100))
    description = Column(String())
