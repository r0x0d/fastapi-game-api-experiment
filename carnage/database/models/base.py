import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr


class BaseMixin:
    __name__ = "BaseMixin"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime, default=None, nullable=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


BaseModel = declarative_base(cls=BaseMixin)
