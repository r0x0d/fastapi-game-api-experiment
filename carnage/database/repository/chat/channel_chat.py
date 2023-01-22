"""Module that represents the Channel Chat repository."""

from carnage.database.models.chat import ChannelChatModel
from carnage.database.repository.base import BaseRepository


class ChannelChatRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[ChannelChatModel] = ChannelChatModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
