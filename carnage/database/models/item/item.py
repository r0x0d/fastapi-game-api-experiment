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
"""Module that represents the Item Model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class ItemModel(BaseModel):
    """A model-class that represents an Item."""

    __tablename__ = "items"

    name = Column(String(100))
    description = Column(String())
    strength = Column(Integer())
    dexterity = Column(Integer())
    intelligence = Column(Integer())
    base_damage = Column(Integer())
    base_magical_damage = Column(Integer())
    base_armor_resistance = Column(Integer())
    base_magical_resistance = Column(Integer())

    # ForeignKeys
    item_rarity_id = Column(
        UUID(as_uuid=True),
        ForeignKey("item_rarities.id"),
    )
    item_base_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("item_base_types.id"),
    )
    item_magical_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("item_magical_types.id"),
        nullable=True,
    )
