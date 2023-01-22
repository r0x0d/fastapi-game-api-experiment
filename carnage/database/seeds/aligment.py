"""Module that represents the Aligment seeding."""

from carnage.database.repository.aligment import AligmentRepository
from carnage.database.seeds.base import BaseSeed


class AligmentSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "aligment"
    data: list[dict[str, str]] = [
        {
            "name": "Good",
        },
        {
            "name": "Evil",
        },
        {
            "name": "Chaotic",
        },
    ]

    def __init__(
        self,
        repository: type[AligmentRepository] = AligmentRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
