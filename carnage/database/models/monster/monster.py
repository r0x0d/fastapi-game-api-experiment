from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from carnage.database.models.base import BaseModel


class MonsterModel(BaseModel):
    __tablename__ = "monsters"

    name = Column(String(100))
    description = Column(String())
    hitpoints = Column(Integer())
    strength = Column(Integer())
    dexterity = Column(Integer())
    intelligence = Column(Integer())
    base_damage = Column(Integer())
    base_magical_damage = Column(Integer())
    base_armor_resistance = Column(Integer())
    base_magical_resistance = Column(Integer())
    is_boss = Column(Boolean(), nullable=False, default=False)

    # ForeignKeys
    monster_type_id = Column(
        UUID(as_uuid=True),
        ForeignKey("monster_types.id"),
    )
    size_id = Column(UUID(as_uuid=True), ForeignKey("sizes.id"))
    aligment_id = Column(UUID(as_uuid=True), ForeignKey("aligments.id"))
