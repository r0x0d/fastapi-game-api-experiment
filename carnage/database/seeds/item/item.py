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
"""Module that represents the Item seeding."""

from typing import Any

from carnage.database.repository.item import (
    ItemBaseTypeRepository,
    ItemMagicalTypeRepository,
    ItemRarityRepository,
    ItemRepository,
)
from carnage.database.seeds.base import BaseSeed


class ItemSeed(BaseSeed):
    """Class that overrides the base seed methods."""

    name: str = "item"
    data: list[dict[str, Any]] = [
        {
            "name": "Test",
            "description": "Test description",
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "base_damage": 10,
            "base_magical_damage": 10,
            "base_armor_resistance": 10,
            "base_magical_resistance": 10,
        },
    ]

    def __init__(
        self,
        repository: type[ItemRepository] = ItemRepository,
    ) -> None:
        """Default class constructor.

        :param repository: The repository used to issue queries.
        """
        super().__init__(repository=repository)
        self.item_rarity_repository = ItemRarityRepository()
        self.item_base_type_repository = ItemBaseTypeRepository()
        self.item_magical_type_repository = ItemMagicalTypeRepository()

    def seed(self) -> None:
        """Method to seed data into the database."""
        item_rarity = self.item_rarity_repository.select_first()
        item_base_type = self.item_base_type_repository.select_first()
        item_magical_type = self.item_magical_type_repository.select_first()

        for item in self.data:
            item.update(
                {
                    "item_rarity_id": item_rarity[0].id,
                    "item_base_type_id": item_base_type[0].id,
                    "item_magical_type_id": item_magical_type[0].id,
                },
            )

        super().seed()
