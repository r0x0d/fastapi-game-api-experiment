"""Module that represents the Base Model."""

import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base


class BaseMixin:
    """A mixin class that gathers the default columns for any models."""

    __name__ = "BaseMixin"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime, default=None, nullable=True)


BaseModel = declarative_base(cls=BaseMixin)
