from carnage.database.models.condition import ConditionModel
from carnage.database.repository.base import BaseRepository


class ConditionRepository(BaseRepository):
    def __init__(
        self,
        model: type[ConditionModel] = ConditionModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
