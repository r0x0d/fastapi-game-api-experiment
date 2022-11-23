from typing import Type

from carnage.database.repository.chat import ChannelChatRepository
from carnage.database.seeds.base import BaseSeed


class ChannelChatSeed(BaseSeed):
    name: str = "channel_chat"
    data: list[dict[str, str]] = [
        {
            "name": "General",
            "description": "General chat channel",
        },
        {"name": "Help", "description": "Help chat channel"},
    ]

    def __init__(
        self,
        repository: Type[ChannelChatRepository] = ChannelChatRepository,
    ) -> None:
        super().__init__(repository=repository)
