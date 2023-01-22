"""Module that represents the Vocation Spell Model."""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class VocationSpellModel(BaseModel):
    """A model-class that represents an Vocation Spell."""

    __tablename__ = "vocation_spells"

    spell_order = Column(Integer())

    # ForeignKeys
    vocation_id = Column(
        UUID(as_uuid=True),
        ForeignKey("vocations.id"),
    )
    spell_id = Column(UUID(as_uuid=True), ForeignKey("spells.id"))
