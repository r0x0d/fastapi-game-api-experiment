from functools import cached_property
from typing import Any

from carnage.players.vocations.base import BaseVocation
from carnage.players.vocations.knight import Knight


class VocationManager:
    @cached_property
    def _vocation_mapping(self) -> dict[str, Any]:
        """Method that maps the available vocations to their simplified name.

        :return: A dictionary with the seed name as key and a seed class
            instance as value.
        """
        # TODO(r0x0d): Change type annotation for this property in the future
        # for `BaseVocation`
        return {"knight": Knight}

    def select(self, vocation: str) -> BaseVocation | None:
        """Select an vocation out of the list of available ones and return it.

        :param vocation: The name of the vocation to be selected.
        """
        return self._vocation_mapping.get(vocation)
