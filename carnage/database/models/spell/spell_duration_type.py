from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SpellDurationTypeModel(BaseModel):
    __tablename__ = "spell_duration_types"

    name = Column(String(100))
    description = Column(String(100))
