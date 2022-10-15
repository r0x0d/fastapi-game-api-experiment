from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class AligmentModel(BaseModel):
    __tablename__ = "aligments"

    name = Column(String(100))
