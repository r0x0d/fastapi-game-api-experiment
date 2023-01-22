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
"""Module that represents the Race seeding."""

from typing import Any

from carnage.database.repository.aligment import AligmentRepository
from carnage.database.repository.race import RaceRepository
from carnage.database.repository.size import SizeRepository
from carnage.database.seeds.base import BaseSeed


class RaceSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "race"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
        },
    ]

    def __init__(
        self,
        repository: type[RaceRepository] = RaceRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.size_repository = SizeRepository()
        self.aligment_repository = AligmentRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
        aligment = self.aligment_repository.select_first()
        size = self.size_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "aligment_id": aligment[0].id,
                    "size_id": size[0].id,
                },
            )

        super().seed()
