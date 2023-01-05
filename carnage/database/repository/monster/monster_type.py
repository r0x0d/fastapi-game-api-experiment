from carnage.database.models.base import BaseModel
from carnage.database.models.monster import MonsterTypeModel
from carnage.database.repository.base import BaseRepository


class MonsterTypeRepository(BaseRepository):
    def __init__(self, model: BaseModel = MonsterTypeModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
