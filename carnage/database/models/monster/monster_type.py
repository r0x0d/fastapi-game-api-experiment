"""Module that represents the Monster Type Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class MonsterTypeModel(BaseModel):
    """A model-class that represents an Monster Type."""

    __tablename__ = "monster_types"

    name = Column(String(100))
    description = Column(String(100))
