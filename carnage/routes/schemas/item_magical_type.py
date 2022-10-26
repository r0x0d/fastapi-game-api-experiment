from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListItemMagicalTypeSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateItemMagicalTypeSchema(BaseModel):
    name: str
    description: str | None


class CreateItemMagicalTypeSchema(BaseModel):
    name: str
    description: str | None
