from sqlalchemy import Boolean, Column, String

from carnage.database.models.base import BaseModel


class ConditionModel(BaseModel):
    __tablename__ = "conditions"

    name = Column(String(100))
    description = Column(String(100))
    is_permanent = Column(Boolean())
