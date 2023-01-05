from typing import Type

from carnage.database.models.vocation import VocationModel
from carnage.database.repository.base import BaseRepository


class VocationRepository(BaseRepository):
    def __init__(self, model: Type[VocationModel] = VocationModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
