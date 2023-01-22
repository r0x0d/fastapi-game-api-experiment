"""Module that represents the Global Chat repository."""

from carnage.database.models.chat import GlobalChatModel
from carnage.database.repository.base import BaseRepository


class GlobalChatRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[GlobalChatModel] = GlobalChatModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
