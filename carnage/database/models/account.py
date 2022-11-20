import enum

from sqlalchemy import Column, Enum, String

from carnage.database.models.base import BaseModel


class ProviderEnum(enum.Enum):
    google = 1
    github = 2
    gitlab = 3


class AccountModel(BaseModel):
    __tablename__ = "accounts"

    username = Column(String(100))
    nickname = Column(String(100))
    provider = Column(Enum(ProviderEnum))
    secret_key = Column(String(100))
