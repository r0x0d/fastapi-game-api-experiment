"""Module that represents the Global Chat Model."""

import enum

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class ChannelEnum(enum.Enum):
    """An enum that represents the available channels for global chat."""

    general = 1


class GlobalChatModel(BaseModel):
    """A model-class that represents an Global Chat."""

    __tablename__ = "global_chats"

    message = Column(String(100))

    # ForeignKeys
    channel_chat_id = Column(
        UUID(as_uuid=True),
        ForeignKey("channel_chats.id"),
    )
    from_account_id = Column(
        UUID(as_uuid=True),
        ForeignKey("accounts.id"),
    )
