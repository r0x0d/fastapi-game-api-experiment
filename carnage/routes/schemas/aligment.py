from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListAligmentSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateAligmentSchema(BaseModel):
    name: str
    description: str | None


class CreateAligmentSchema(BaseModel):
    name: str
    description: str | None
