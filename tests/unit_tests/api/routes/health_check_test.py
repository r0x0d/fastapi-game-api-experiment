import pytest
from httpx import AsyncClient

from tests.unit_tests.conftest import APPLICATION_PREFIX

BASE_URL = f"http://test/{APPLICATION_PREFIX}/health_check"


@pytest.mark.anyio
async def test_get(application_instance, get_fake_jwt):
    async with AsyncClient(app=application_instance, base_url=BASE_URL) as ac:
        response = await ac.get("/")

        assert response.status_code == 200
        assert isinstance(response.json(), dict)
        assert len(response.json()) > 0
        assert "alive" in response.json()
        assert {"alive": True} == response.json()
