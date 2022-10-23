import uuid
from collections import namedtuple
from unittest import mock

import pytest
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

from carnage.application import create_app
from carnage.database.repository import base

BaseModel = declarative_base()


class DummySqlModel(BaseModel):
    __tablename__ = "DummySqlModel"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String())


DummySchemaFields = namedtuple(
    "DummySchemaFields",
    ("id", "created_at", "updated_at", "deleted_at"),
)


@pytest.fixture()
def database_session_mock(monkeypatch):
    monkeypatch.setattr(base, "session", mock.MagicMock())


@pytest.fixture()
def application_instance():
    return create_app()


@pytest.fixture
def anyio_backend():
    return "asyncio"
