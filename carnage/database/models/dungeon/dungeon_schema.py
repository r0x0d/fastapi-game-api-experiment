"""Module that represents the Dungeon Schema Model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class DungeonSchemaModel(BaseModel):
    """A model-class that represents an Dungeon Schema."""

    __tablename__ = "dungeon_schemas"

    name = Column(String(100))
    description = Column(String())
    schema = Column(String())
    version = Column(Integer(), nullable=False)

    # ForeignKeys
    dungeon_difficulty_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dungeon_difficulties.id"),
    )
