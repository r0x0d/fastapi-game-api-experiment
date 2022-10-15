from uuid import UUID

from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListMonsterSchema(BaseSchema):
    name: str
    description: str | None
    hitpoints: int
    strength: int
    dexterity: int
    intelligence: int
    base_damage: int
    base_magical_damage: int
    base_armor_resistance: int
    base_magical_resistance: int

    monster_type_id: UUID
    size_id: UUID
    aligment_id: UUID

    class Config:
        orm_mode = True


class UpdateMonsterSchema(BaseModel):
    name: str
    description: str | None
    hitpoints: int
    strength: int
    dexterity: int
    intelligence: int
    base_damage: int
    base_magical_damage: int
    base_armor_resistance: int
    base_magical_resistance: int

    monster_type_id: UUID
    size_id: UUID
    aligment_id: UUID


class CreateMonsterSchema(BaseModel):
    name: str
    description: str | None
    hitpoints: int
    strength: int
    dexterity: int
    intelligence: int
    base_damage: int
    base_magical_damage: int
    base_armor_resistance: int
    base_magical_resistance: int

    monster_type_id: UUID
    size_id: UUID
    aligment_id: UUID
