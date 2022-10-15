from carnage.database.models.base import BaseModel
from carnage.database.models.size import SizeModel
from carnage.database.repository.base import BaseRepository


class SizeRepository(BaseRepository):
    def __init__(self, model: BaseModel = SizeModel) -> None:
        super().__init__(model)
