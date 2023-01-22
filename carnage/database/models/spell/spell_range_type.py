"""Module that represents the Spell Range Type Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SpellRangeTypeModel(BaseModel):
    """A model-class that represents an Spell Range Type."""

    __tablename__ = "spell_range_types"

    name = Column(String(100))
    description = Column(String(100))
