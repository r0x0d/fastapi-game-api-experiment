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
"""Module that represents the Spell Model."""

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class SpellModel(BaseModel):
    """A model-class that represents an Spell."""

    __tablename__ = "spells"

    name = Column(String(100), nullable=False)
    description = Column(String(), nullable=False)
    base_damage = Column(Integer(), nullable=False)
    base_magical_damage = Column(Integer(), nullable=False)
    attack_threshold = Column(Float(), nullable=False)
    critical_attack_threshold = Column(Float(), nullable=False)

    # ForeignKeys
    spell_duration_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("spell_duration_types.id"),
    )
    spell_range_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("spell_range_types.id"),
    )
    spell_school_id = Column(
        UUID(as_uuid=True),
        ForeignKey("spell_schools.id"),
    )
