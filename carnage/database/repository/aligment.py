"""Module that represents the Aligment repository."""

from carnage.database.models.aligment import AligmentModel
from carnage.database.models.base import BaseModel
from carnage.database.repository.base import BaseRepository


class AligmentRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: BaseModel = AligmentModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
