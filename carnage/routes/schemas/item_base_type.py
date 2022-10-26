from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListItemBaseTypeSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateItemBaseTypeSchema(BaseModel):
    name: str
    description: str | None


class CreateItemBaseTypeSchema(BaseModel):
    name: str
    description: str | None
