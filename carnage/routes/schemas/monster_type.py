from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListMonsterTypeSchema(BaseSchema):
    name: str
    description: str | None

    class Config:
        orm_mode = True


class UpdateMonsterTypeSchema(BaseModel):
    name: str
    description: str | None


class CreateMonsterTypeSchema(BaseModel):
    name: str
    description: str | None
