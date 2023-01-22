"""Module that represents the Game Mode Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class GameModeModel(BaseModel):
    """A model-class that represents an Game Mode."""

    __tablename__ = "game_modes"

    name = Column(String(100))
    description = Column(String())
