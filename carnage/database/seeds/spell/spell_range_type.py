# MIT License
#
# Copyright (c) 2022, Rodolfo Olivieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Module that represents the Spell Range Type seeding."""

from carnage.database.repository.spell import SpellRangeTypeRepository
from carnage.database.seeds.base import BaseSeed


class SpellRangeTypeSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "spell-range-type"
    data: list[dict[str, str]] = [
        {
            "name": "Self",
            "description": "Self range",
        },
        {
            "name": "Touch",
            "description": "Touch range",
        },
        {
            "name": "Ranged",
            "description": "Ranged range",
        },
        {
            "name": "Sight",
            "description": "Sight range",
        },
        {
            "name": "Unlimited",
            "description": "Unlimited range",
        },
    ]

    def __init__(
        self,
        repository: type[SpellRangeTypeRepository] = SpellRangeTypeRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
