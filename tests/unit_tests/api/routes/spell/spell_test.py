from collections import namedtuple
from datetime import datetime
from unittest import mock
from uuid import uuid4

import pytest
from httpx import AsyncClient

from carnage.api.routes.spell.spell import route
from tests.unit_tests.conftest import APPLICATION_PREFIX, DummySchemaFields

SpellOutput = namedtuple(
    "SpellOutput",
    (
        *DummySchemaFields._fields,
        "name",
        "description",
        "base_damage",
        "base_magical_damage",
        "attack_threshold",
        "critical_attack_threshold",
        "spell_school_id",
        "spell_duration_type_id",
        "spell_range_type_id",
    ),
)
BASE_URL = f"http://test/{APPLICATION_PREFIX}/spell"


@pytest.mark.anyio()
@pytest.mark.parametrize(
    ("output"),
    (
        (
            [
                SpellOutput(
                    id=uuid4(),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    name="test_name",
                    description="test_description",
                    base_damage=10,
                    base_magical_damage=10,
                    attack_threshold=10,
                    critical_attack_threshold=10,
                    spell_school_id=uuid4(),
                    spell_duration_type_id=uuid4(),
                    spell_range_type_id=uuid4(),
                ),
            ]
        ),
    ),
)
async def test_get(output, application_instance, get_fake_jwt):
    with mock.patch.object(
        route.repository,
        "select",
        lambda: output,
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
            headers={"Authorization": f"Bearer {get_fake_jwt}"},
        ) as ac:
            response = await ac.get("/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0


@pytest.mark.anyio()
@pytest.mark.parametrize(
    ("output"),
    (
        (
            [
                SpellOutput(
                    id=uuid4(),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                    deleted_at=None,
                    name="test_name",
                    description="test_description",
                    base_damage=10,
                    base_magical_damage=10,
                    attack_threshold=10,
                    critical_attack_threshold=10,
                    spell_school_id=uuid4(),
                    spell_duration_type_id=uuid4(),
                    spell_range_type_id=uuid4(),
                ),
            ]
        ),
    ),
)
async def test_get_by_id(output, application_instance, get_fake_jwt):
    with mock.patch.object(
        route.repository,
        "select_by_id",
        lambda identifier: output,
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
            headers={"Authorization": f"Bearer {get_fake_jwt}"},
        ) as ac:
            response = await ac.get("/26609c62-5270-11ed-8d79-641c67e34d72")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)


@pytest.mark.anyio()
@pytest.mark.parametrize(
    ("data"),
    (
        (
            {
                "name": "test_name",
                "description": "test_description",
                "base_damage": 10,
                "base_magical_damage": 10,
                "attack_threshold": 10,
                "critical_attack_threshold": 10,
                "spell_school_id": str(uuid4()),
                "spell_duration_type_id": str(uuid4()),
                "spell_range_type_id": str(uuid4()),
            }
        ),
    ),
)
async def test_post(data, application_instance, get_fake_jwt):
    with mock.patch.object(
        route.repository,
        "insert",
        lambda values: None,
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
            headers={"Authorization": f"Bearer {get_fake_jwt}"},
        ) as ac:
            response = await ac.post("/", json=data)
        assert response.status_code == 201


@pytest.mark.anyio()
@pytest.mark.parametrize(
    ("data"),
    (
        (
            {
                "name": "test_name",
                "description": "test_description",
                "base_damage": 10,
                "base_magical_damage": 10,
                "attack_threshold": 10,
                "critical_attack_threshold": 10,
                "spell_school_id": str(uuid4()),
                "spell_duration_type_id": str(uuid4()),
                "spell_range_type_id": str(uuid4()),
            }
        ),
    ),
)
async def test_put(data, application_instance, get_fake_jwt):
    with mock.patch.object(
        route.repository,
        "update",
        lambda values, identifier: None,
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
            headers={"Authorization": f"Bearer {get_fake_jwt}"},
        ) as ac:
            response = await ac.put(
                "/26609c62-5270-11ed-8d79-641c67e34d72",
                json=data,
            )
    assert response.status_code == 204


@pytest.mark.anyio()
async def test_delete(application_instance, get_fake_jwt):
    with mock.patch.object(
        route.repository,
        "delete",
        lambda identifier: None,
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
            headers={"Authorization": f"Bearer {get_fake_jwt}"},
        ) as ac:
            response = await ac.delete("/26609c62-5270-11ed-8d79-641c67e34d72")
        assert response.status_code == 204
