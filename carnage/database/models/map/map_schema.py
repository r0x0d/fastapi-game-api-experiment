from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from carnage.database.models.base import BaseModel


class MapSchemaModel(BaseModel):
    __tablename__ = "map_schemas"

    name = Column(String(100))
    description = Column(String())
    schema = Column(JSONB(none_as_null=False))

    # ForeignKeys
    map_difficulty_id = Column(
        UUID(as_uuid=True),
        ForeignKey("map_difficulties.id"),
    )
