from typing import Any, Type

from carnage.database.repository.game_mode import GameModeRepository
from carnage.database.seeds.base import BaseSeed


class GameModeSeed(BaseSeed):
    name: str = "game_mode"
    data: list[dict[str, Any]] = [
        {
            "name": "Normal",
            "description": "Normal game mode. Recommended for new players.",
        },
        {
            "name": "Carnage",
            "description": "Where your nightmares come true.",
        },
    ]

    def __init__(
        self,
        repository: Type[GameModeRepository] = GameModeRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
