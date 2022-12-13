from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class DifficultyModel(BaseModel):
    __tablename__ = "difficulties"

    name = Column(String(100))
    description = Column(String())
