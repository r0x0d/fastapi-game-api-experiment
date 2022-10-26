from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListSpellSchoolSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateSpellSchoolSchema(BaseModel):
    name: str
    description: str | None


class CreateSpellSchoolSchema(BaseModel):
    name: str
    description: str | None
