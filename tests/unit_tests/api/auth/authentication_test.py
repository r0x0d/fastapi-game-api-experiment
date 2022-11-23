from collections import namedtuple
from time import time
from unittest import mock

import pytest
from fastapi import HTTPException
from jose import ExpiredSignatureError

from carnage.api.auth import authentication

APIJWTBearerOutput = namedtuple("APIJWTBearerOutput", ("headers"))


@pytest.mark.parametrize(
    ("claims"),
    (
        ({"email": "test@test.com"}),
        ({"email": "tets@test.com", "aud": time()}),
        ({"email": "tets@test.com", "at_hash": "test_hash"}),
    ),
)
def test_generate_jwt(claims):
    result = authentication.generate_jwt(claims)
    assert result is not None


@pytest.mark.anyio
async def test_api_jwt_bearer_call(get_fake_jwt):
    request = APIJWTBearerOutput({"Authorization": f"Bearer {get_fake_jwt}"})
    result = await authentication.APIJWTBearer().__call__(request)
    assert result


@pytest.mark.anyio
async def test_api_jwt_bearer_call_wrong_scheme(get_fake_jwt):
    request = APIJWTBearerOutput({"Authorization": f"test {get_fake_jwt}"})
    with pytest.raises(HTTPException):
        await authentication.APIJWTBearer().__call__(request)


@pytest.mark.anyio
async def test_api_jwt_bearer__call_invalid_token():
    token = authentication.generate_jwt(
        claims={"email": "test@test.com"},
    )
    request = APIJWTBearerOutput({"Authorization": f"Bearer {token}"})
    with mock.patch.object(
        authentication.jwt,
        "decode",
        side_effect=ExpiredSignatureError,
    ):

        with pytest.raises(HTTPException):
            await authentication.APIJWTBearer().__call__(request)


@pytest.mark.anyio
async def test_api_jwt_bearer__call_invalid_authorization_code(get_fake_jwt):
    request = APIJWTBearerOutput({"Authorization": f"test {get_fake_jwt}"})
    with pytest.raises(HTTPException):
        await authentication.APIJWTBearer(auto_error=False).__call__(request)


@pytest.mark.parametrize(
    ("use_fake_jwt", "expected"),
    (
        (True, True),
        (False, False),
    ),
)
def test_api_jwt_bearer_verify_jwt(use_fake_jwt, expected, get_fake_jwt):
    token = (
        get_fake_jwt
        if use_fake_jwt
        else authentication.generate_jwt(
            claims={"email": "test@test.com"},
        )
    )
    if use_fake_jwt:
        assert authentication.APIJWTBearer().verify_jwt(token) == expected
    else:
        with mock.patch.object(
            authentication.jwt,
            "decode",
            side_effect=ExpiredSignatureError,
        ):
            assert authentication.APIJWTBearer().verify_jwt(token) == expected


@pytest.mark.anyio
async def test_websocket_jwt_bearer_call(get_fake_jwt):
    result = await authentication.WebSocketJWTBearer().__call__(get_fake_jwt)
    assert result


@pytest.mark.anyio
async def test_websocket_jwt_bearer__call_invalid_token():
    token = authentication.generate_jwt(
        claims={"email": "test@test.com"},
    )
    with mock.patch.object(
        authentication.jwt,
        "decode",
        side_effect=ExpiredSignatureError,
    ):

        with pytest.raises(HTTPException):
            await authentication.WebSocketJWTBearer().__call__(token)


@pytest.mark.anyio
async def test_websocket_websocket_jwt_bearer__call_no_token_provided(
    get_fake_jwt,
):
    with pytest.raises(HTTPException):
        await authentication.WebSocketJWTBearer(auto_error=False).__call__(
            None,
        )
