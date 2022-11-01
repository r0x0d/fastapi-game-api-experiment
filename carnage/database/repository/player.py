from typing import Type

from carnage.database.models.player import PlayerModel
from carnage.database.repository.base import BaseRepository


class PlayerRepository(BaseRepository):
    def __init__(self, model: Type[PlayerModel] = PlayerModel) -> None:
        super().__init__(model)