"""Module that represents the Player Model."""

from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class PlayerModel(BaseModel):
    """A model-class that represents an Player."""

    __tablename__ = "players"

    name = Column(String(100))
    description = Column(String())
    is_alive = Column(Boolean())
    # ForeignKeys
    dungeon_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dungeons.id"),
    )
    vocation_id = Column(UUID(as_uuid=True), ForeignKey("vocations.id"))
