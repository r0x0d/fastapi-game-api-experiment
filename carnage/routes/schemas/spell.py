from uuid import UUID

from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListSpellSchema(BaseSchema):
    name: str
    description: str | None

    spell_duration_type_id: UUID
    spell_range_type_id: UUID
    spell_school_id: UUID

    class Config:
        orm_mode = True


class UpdateSpellSchema(BaseModel):
    name: str
    description: str | None

    spell_duration_type_id: UUID
    spell_range_type_id: UUID
    spell_school_id: UUID


class CreateSpellSchema(BaseModel):
    name: str
    description: str | None

    spell_duration_type_id: UUID
    spell_range_type_id: UUID
    spell_school_id: UUID
