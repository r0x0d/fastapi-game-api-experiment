"""Module that represents a Knight vocation."""
from carnage.database.models.vocation.vocation import VocationModel
from carnage.players.vocations.base import BaseVocation


class Knight(BaseVocation):
    """Class that overrides methods and properties of vocation."""

    def __init__(self, vocation: VocationModel) -> None:
        """Class that interprets an specific player.

        :param vocation: The model that represents a vocation.
        """
        super().__init__(vocation)
