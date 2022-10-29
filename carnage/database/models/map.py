from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB, UUID

from carnage.database.models.base import BaseModel


class MapModel(BaseModel):
    __tablename__ = "maps"

    name = Column(String(100))
    description = Column(String())
    plot = Column(JSONB(none_as_null=False))

    # ForeignKeys
    map_schema_id = Column(
        UUID(as_uuid=True),
        ForeignKey("map_schemas.id"),
    )
