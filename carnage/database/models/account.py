import enum

from sqlalchemy import Column, Enum, String

from carnage.database.models.base import BaseModel


class ProviderEnum(enum.Enum):
    carnage = 0
    google = 1
    github = 2
    twitter = 3


class AccountModel(BaseModel):
    __tablename__ = "accounts"

    username = Column(String(100))
    password = Column(String(100))
    provider = Column(Enum(ProviderEnum))
    secret_key = Column(String(100))
