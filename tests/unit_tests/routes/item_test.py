from collections import namedtuple
from datetime import datetime
from uuid import uuid4

import pytest
from httpx import AsyncClient

from carnage.routes import item
from tests.unit_tests.conftest import APPLICATION_PREFIX, DummySchemaFields

ItemOutput = namedtuple(
    "ItemOutput",
    (
        *DummySchemaFields._fields,
        "name",
        "description",
        "strength",
        "intelligence",
        "dexterity",
        "base_damage",
        "base_magical_damage",
        "base_armor_resistance",
        "base_magical_resistance",
        "item_rarity_id",
        "item_base_type_id",
        "item_magical_type_id",
    ),
)
BASE_URL = f"http://test/{APPLICATION_PREFIX}/item"


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("output"),
    (
        (
            [
                ItemOutput(
                    id=uuid4(),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    name="test_name",
                    description="test_description",
                    strength=10,
                    intelligence=10,
                    dexterity=10,
                    base_damage=10,
                    base_magical_damage=10,
                    base_armor_resistance=10,
                    base_magical_resistance=10,
                    item_rarity_id=uuid4(),
                    item_base_type_id=uuid4(),
                    item_magical_type_id=uuid4(),
                ),
            ]
        ),
    ),
)
async def test_get(output, application_instance, monkeypatch):
    monkeypatch.setattr(
        item.repository,
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
                ItemOutput(
                    id=uuid4(),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    name="test_name",
                    description="test_description",
                    strength=10,
                    intelligence=10,
                    dexterity=10,
                    base_damage=10,
                    base_magical_damage=10,
                    base_armor_resistance=10,
                    base_magical_resistance=10,
                    item_rarity_id=uuid4(),
                    item_base_type_id=uuid4(),
                    item_magical_type_id=uuid4(),
                ),
            ]
        ),
    ),
)
async def test_get_by_id(output, application_instance, monkeypatch):
    monkeypatch.setattr(
        item.repository,
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
                "strength": 10,
                "intelligence": 10,
                "dexterity": 10,
                "base_damage": 10,
                "base_magical_damage": 10,
                "base_armor_resistance": 10,
                "base_magical_resistance": 10,
                "item_rarity_id": str(uuid4()),
                "item_base_type_id": str(uuid4()),
                "item_magical_type_id": str(uuid4()),
            }
        ),
    ),
)
async def test_post(data, application_instance, monkeypatch):
    monkeypatch.setattr(
        item.repository,
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
                "strength": 10,
                "intelligence": 10,
                "dexterity": 10,
                "base_damage": 10,
                "base_magical_damage": 10,
                "base_armor_resistance": 10,
                "base_magical_resistance": 10,
                "item_rarity_id": str(uuid4()),
                "item_base_type_id": str(uuid4()),
                "item_magical_type_id": str(uuid4()),
            }
        ),
    ),
)
async def test_put(data, application_instance, monkeypatch):
    monkeypatch.setattr(
        item.repository,
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
        item.repository,
        "delete",
        lambda identifier: None,
    )
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.delete("/26609c62-5270-11ed-8d79-641c67e34d72")
    assert response.status_code == 204
