"""Module that represents the Spell Model."""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class SpellModel(BaseModel):
    """A model-class that represents an Spell."""

    __tablename__ = "spells"

    name = Column(String(100))
    description = Column(String())

    # ForeignKeys
    spell_duration_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("spell_duration_types.id"),
    )
    spell_range_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("spell_range_types.id"),
    )
    spell_school_id = Column(
        UUID(as_uuid=True),
        ForeignKey("spell_schools.id"),
    )
