from carnage.database.models.dungeon import DungeonModel
from carnage.database.repository.base import BaseRepository


class DungeonRepository(BaseRepository):
    def __init__(self, model: type[DungeonModel] = DungeonModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
