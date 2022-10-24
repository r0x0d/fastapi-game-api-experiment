from pydantic import BaseModel

from carnage.routes.schemas.base import BaseSchema


class ListAccountSchema(BaseSchema):
    username: str
    provider: str

    class Config:
        orm_mode = True


class UpdateAccountSchema(BaseModel):
    username: str
    password: str | None


class CreateAccountSchema(BaseModel):
    username: str
    password: str | None
    provider: str = "carnage"
