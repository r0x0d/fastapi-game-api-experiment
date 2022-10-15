from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, validator


class BaseSchema(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    @validator("id")
    def identifier_as_str(cls, identifier: UUID) -> str:
        return str(identifier)
