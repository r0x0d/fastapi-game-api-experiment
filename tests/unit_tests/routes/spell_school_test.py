from collections import namedtuple
from datetime import datetime
from uuid import uuid4

import pytest
from httpx import AsyncClient

from carnage.routes import spell_school
from tests.unit_tests.conftest import APPLICATION_PREFIX, DummySchemaFields

SpellSchoolOutput = namedtuple(
    "SpellSchoolOutput",
    (*DummySchemaFields._fields, "name", "description"),
)
BASE_URL = f"http://test/{APPLICATION_PREFIX}/spell_school"


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("output"),
    (
        (
            [
                SpellSchoolOutput(
                    id=uuid4(),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    name="test_name",
                    description="test_description",
                ),
            ]
        ),
    ),
)
async def test_get(output, application_instance, monkeypatch):
    monkeypatch.setattr(
        spell_school.repository,
        "select",
        lambda: output,
    )
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("output"),
    (
        (
            [
                SpellSchoolOutput(
                    id=uuid4(),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    name="test_name",
                    description="test_description",
                ),
            ]
        ),
    ),
)
async def test_get_by_id(output, application_instance, monkeypatch):
    monkeypatch.setattr(
        spell_school.repository,
        "select_by_id",
        lambda identifier: output,
    )
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.get("/26609c62-5270-11ed-8d79-641c67e34d72")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("data"),
    (
        (
            {
                "name": "test_name",
                "description": "test_description",
            }
        ),
    ),
)
async def test_post(data, application_instance, monkeypatch):
    monkeypatch.setattr(
        spell_school.repository,
        "insert",
        lambda values: None,
    )
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.post("/", json=data)
    assert response.status_code == 201


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("data"),
    (
        (
            {
                "name": "test_name",
                "description": "test_description",
            }
        ),
    ),
)
async def test_put(data, application_instance, monkeypatch):
    monkeypatch.setattr(
        spell_school.repository,
        "update",
        lambda values, identifier: None,
    )
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.put(
            "/26609c62-5270-11ed-8d79-641c67e34d72",
            json=data,
        )
    assert response.status_code == 204


@pytest.mark.anyio
async def test_delete(application_instance, monkeypatch):
    monkeypatch.setattr(
        spell_school.repository,
        "delete",
        lambda identifier: None,
    )
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.delete("/26609c62-5270-11ed-8d79-641c67e34d72")
    assert response.status_code == 204
