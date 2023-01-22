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
