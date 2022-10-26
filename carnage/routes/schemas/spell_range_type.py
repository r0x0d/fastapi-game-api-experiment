from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListSpellRangeTypeSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateSpellRangeTypeSchema(BaseModel):
    name: str
    description: str | None


class CreateSpellRangeTypeSchema(BaseModel):
    name: str
    description: str | None
