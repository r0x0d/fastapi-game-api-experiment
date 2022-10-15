from carnage.database.models.base import BaseModel
from carnage.database.models.monster_type import MonsterTypeModel
from carnage.database.repository.base import BaseRepository


class MonsterTypeRepository(BaseRepository):
    def __init__(self, model: BaseModel = MonsterTypeModel) -> None:
        super().__init__(model)
