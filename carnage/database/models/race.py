"""Module that represents the Race Model."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class RaceModel(BaseModel):
    """A model-class that represents an Race."""

    __tablename__ = "races"

    name = Column(String(100))
    description = Column(String())

    # ForeignKeys
    size_id = Column(UUID(as_uuid=True), ForeignKey("sizes.id"))
    aligment_id = Column(UUID(as_uuid=True), ForeignKey("aligments.id"))
