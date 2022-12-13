from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class GameModeModel(BaseModel):
    __tablename__ = "game_modes"

    name = Column(String(100))
    description = Column(String())
