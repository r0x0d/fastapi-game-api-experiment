"""Module that represents the Dungeon Difficulty Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class DungeonDifficultyModel(BaseModel):
    """A model-class that represents an Dungeon Difficulty."""

    __tablename__ = "dungeon_difficulties"

    level = Column(String(100))
    description = Column(String())
