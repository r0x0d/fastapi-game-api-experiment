from uuid import UUID

from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListItemSchema(BaseSchema):
    name: str
    description: str | None
    strength: int
    dexterity: int
    intelligence: int
    base_damage: int
    base_magical_damage: int
    base_armor_resistance: int
    base_magical_resistance: int

    item_rarity_id: UUID
    item_base_type_id: UUID
    item_magical_type_id: UUID

    class Config:
        orm_mode = True


class UpdateItemSchema(BaseModel):
    name: str
    description: str | None
    strength: int
    dexterity: int
    intelligence: int
    base_damage: int
    base_magical_damage: int
    base_armor_resistance: int
    base_magical_resistance: int

    item_rarity_id: UUID
    item_base_type_id: UUID
    item_magical_type_id: UUID


class CreateItemSchema(BaseModel):
    name: str
    description: str | None
    strength: int
    dexterity: int
    intelligence: int
    base_damage: int
    base_magical_damage: int
    base_armor_resistance: int
    base_magical_resistance: int

    item_rarity_id: UUID
    item_base_type_id: UUID
    item_magical_type_id: UUID
