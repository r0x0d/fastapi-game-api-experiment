"""Module that represents the Spell Duration Type Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SpellDurationTypeModel(BaseModel):
    """A model-class that represents an Spell Duration Type."""

    __tablename__ = "spell_duration_types"

    name = Column(String(100))
    description = Column(String(100))
