"""Module that represents the Vocation repository."""

from carnage.database.models.vocation import VocationModel
from carnage.database.repository.base import BaseRepository


class VocationRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(self, model: type[VocationModel] = VocationModel) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
