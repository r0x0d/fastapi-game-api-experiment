from typing import Type

from carnage.database.models.game_mode import GameModeModel
from carnage.database.repository.base import BaseRepository


class GameModeRepository(BaseRepository):
    def __init__(self, model: Type[GameModeModel] = GameModeModel) -> None:
        super().__init__(model)
