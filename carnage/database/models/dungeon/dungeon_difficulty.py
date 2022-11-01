from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class DungeonDifficultyModel(BaseModel):
    __tablename__ = "dungeon_difficulties"

    level = Column(String(100))
    description = Column(String())
