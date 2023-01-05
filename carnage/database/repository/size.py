from carnage.database.models.base import BaseModel
from carnage.database.models.size import SizeModel
from carnage.database.repository.base import BaseRepository


class SizeRepository(BaseRepository):
    def __init__(self, model: BaseModel = SizeModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
