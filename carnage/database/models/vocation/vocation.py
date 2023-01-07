from sqlalchemy import Column, Float, Integer, String

from carnage.database.models.base import BaseModel


class VocationModel(BaseModel):
    __tablename__ = "vocations"

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
    attack_threshold = Column(Float(), nullable=False)
    critical_attack_threshold = Column(Float(), nullable=False)
