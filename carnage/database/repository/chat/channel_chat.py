from typing import Type

from carnage.database.models.chat import ChannelChatModel
from carnage.database.repository.base import BaseRepository


class ChannelChatRepository(BaseRepository):
    def __init__(
        self,
        model: Type[ChannelChatModel] = ChannelChatModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
