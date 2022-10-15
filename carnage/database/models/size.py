from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SizeModel(BaseModel):
    __tablename__ = "sizes"

    name = Column(String(100))
