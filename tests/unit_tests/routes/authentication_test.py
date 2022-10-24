from unittest import mock

import pytest
from httpx import AsyncClient

from carnage.routes import authentication

BASE_URL = "http://test/authentication"


@pytest.mark.anyio
async def test_google_login(application_instance, monkeypatch):
    with mock.patch.object(
        authentication.oauth.google,
        "authorize_access_token",
        mock.AsyncMock(),
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
        ) as ac:
            response = await ac.get("/google/login")
        assert response.status_code == 302


@pytest.mark.anyio
async def test_google_auth(application_instance):

    with mock.patch.object(
        authentication.oauth.google,
        "authorize_access_token",
        mock.AsyncMock(),
    ):
        async with AsyncClient(
            app=application_instance,
            base_url=BASE_URL,
        ) as ac:
            response = await ac.get("/google/auth")
        assert response.status_code == 200
