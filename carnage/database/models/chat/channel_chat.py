from sqlalchemy import Column, String

from carnage.database.models.base import BaseModel


class ChannelChatModel(BaseModel):
    __tablename__ = "channel_chats"

    name = Column(String(100))
    description = Column(String())
