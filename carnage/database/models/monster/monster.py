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
"""Module that represents the Monster Model."""

from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class MonsterModel(BaseModel):
    """A model-class that represents an Monster."""

    __tablename__ = "monsters"

    name = Column(String(100))
    description = Column(String())
    hitpoints = Column(Integer())
    strength = Column(Integer())
    dexterity = Column(Integer())
    intelligence = Column(Integer())
    luck = Column(Integer())
    base_damage = Column(Integer())
    base_magical_damage = Column(Integer())
    base_armor_resistance = Column(Integer())
    base_magical_resistance = Column(Integer())
    is_boss = Column(Boolean(), nullable=False, default=False)
    attack_threshold = Column(Float(), nullable=False)
    critical_attack_threshold = Column(Float(), nullable=False)

    # ForeignKeys
    monster_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("monster_types.id"),
    )
    size_id = Column(UUID(as_uuid=True), ForeignKey("sizes.id"))
    aligment_id = Column(UUID(as_uuid=True), ForeignKey("aligments.id"))
