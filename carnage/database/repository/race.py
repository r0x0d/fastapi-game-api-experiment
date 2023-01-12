from carnage.database.models.race import RaceModel
from carnage.database.repository.base import BaseRepository


class RaceRepository(BaseRepository):
    def __init__(self, model: type[RaceModel] = RaceModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
