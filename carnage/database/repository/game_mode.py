"""Module that represents the Game Mode repository."""

from carnage.database.models.game_mode import GameModeModel
from carnage.database.repository.base import BaseRepository


class GameModeRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: type[GameModeModel] = GameModeModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
