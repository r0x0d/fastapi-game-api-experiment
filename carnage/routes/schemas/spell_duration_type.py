from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListSpellDurationTypeSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateSpellDurationTypeSchema(BaseModel):
    name: str
    description: str | None


class CreateSpellDurationTypeSchema(BaseModel):
    name: str
    description: str | None
