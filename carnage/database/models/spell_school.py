from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SpellSchoolModel(BaseModel):
    __tablename__ = "spell_schools"

    name = Column(String(100))
    description = Column(String(100))
