from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListItemRaritySchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateItemRaritySchema(BaseModel):
    name: str
    description: str | None


class CreateItemRaritySchema(BaseModel):
    name: str
    description: str | None
