"""Module that represents the Spell School Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SpellSchoolModel(BaseModel):
    """A model-class that represents an Spell School."""

    __tablename__ = "spell_schools"

    name = Column(String(100))
    description = Column(String(100))
