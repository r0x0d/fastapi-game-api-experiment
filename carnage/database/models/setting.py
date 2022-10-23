from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class SettingModel(BaseModel):
    __tablename__ = "settings"

    secret_key = Column(String(100))
    environment = Column(String())
