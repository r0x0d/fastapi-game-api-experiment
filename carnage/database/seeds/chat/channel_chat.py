"""Module that represents the Channel Chat seeding."""

from carnage.database.repository.chat import ChannelChatRepository
from carnage.database.seeds.base import BaseSeed


class ChannelChatSeed(BaseSeed):
    """Class that overrides the base seed methods."""

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
        repository: type[ChannelChatRepository] = ChannelChatRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
