from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class MapDifficultyModel(BaseModel):
    __tablename__ = "map_difficulties"

    level = Column(String(100))
    description = Column(String())
