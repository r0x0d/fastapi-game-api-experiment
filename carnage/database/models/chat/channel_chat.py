"""Module that represents the Channel Chat Model."""

from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ChannelChatModel(BaseModel):
    """A model-class that represents an Channel Chat."""

    __tablename__ = "channel_chats"

    name = Column(String(100))
    description = Column(String())
