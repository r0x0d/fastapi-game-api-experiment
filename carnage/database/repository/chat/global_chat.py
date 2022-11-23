from typing import Type

from carnage.database.models.chat import GlobalChatModel
from carnage.database.repository.base import BaseRepository


class GlobalChatRepository(BaseRepository):
    def __init__(
        self,
        model: Type[GlobalChatModel] = GlobalChatModel,
    ) -> None:
        super().__init__(model)
