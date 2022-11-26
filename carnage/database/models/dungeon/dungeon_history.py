from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class DungeonHistoryModel(BaseModel):
    __tablename__ = "dungeon_histories"

    last_level = Column(Integer())
    last_room = Column(Integer())
    is_player_alive = Column(Boolean())
    is_dungeon_complete = Column(Boolean())

    # ForeignKeys
    player_id = Column(
        UUID(as_uuid=True),
        ForeignKey("players.id"),
    )
    dungeon_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dungeons.id"),
    )
