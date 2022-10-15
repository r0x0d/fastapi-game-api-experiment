from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListSizeSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateSizeSchema(BaseModel):
    name: str
    description: str | None


class CreateSizeSchema(BaseModel):
    name: str
    description: str | None
