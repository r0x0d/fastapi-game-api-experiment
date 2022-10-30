from typing import Type

from carnage.database.models.vocation import VocationModel
from carnage.database.repository.base import BaseRepository


class VocationRepository(BaseRepository):
    def __init__(self, model: Type[VocationModel] = VocationModel) -> None:
        super().__init__(model)
