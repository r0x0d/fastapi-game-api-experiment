from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class MonsterTypeModel(BaseModel):
    __tablename__ = "monster_types"

    name = Column(String(100))
    description = Column(String(100))
