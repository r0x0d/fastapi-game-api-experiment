"""Module that represents the Dungeon Model."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from carnage.database.models.base import BaseModel


class DungeonModel(BaseModel):
    """A model-class that represents an Dungeon."""

    __tablename__ = "dungeons"

    name = Column(String(100))
    description = Column(String())
    plot = Column(JSONB(none_as_null=False))

    # ForeignKeys
    dungeon_schema_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dungeon_schemas.id"),
    )
