from collections import namedtuple
from time import time
from unittest import mock

import pytest
from fastapi import HTTPException
from jose import ExpiredSignatureError

from carnage.api.auth import authentication

RequestOutput = namedtuple("RequestOutput", ("headers"))


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


def test_validate_jwt(get_fake_jwt):
    assert authentication.validate_jwt(token=get_fake_jwt)


def test_validate_jwt_expired():
    token = authentication.generate_jwt(
        claims={"email": "test@test.com"},
    )
    with mock.patch.object(
        authentication.jwt,
        "decode",
        side_effect=ExpiredSignatureError,
    ):
        assert not authentication.validate_jwt(token)


@pytest.mark.anyio
async def test_jwt_bearer_call(get_fake_jwt):
    request = RequestOutput({"Authorization": f"Bearer {get_fake_jwt}"})
    result = await authentication.JWTBearer().__call__(request)
    assert result == get_fake_jwt


@pytest.mark.anyio
async def test_jwt_bearer_call_wrong_scheme(get_fake_jwt):
    request = RequestOutput({"Authorization": f"test {get_fake_jwt}"})
    with pytest.raises(HTTPException):
        await authentication.JWTBearer().__call__(request)


@pytest.mark.anyio
async def test_jwt_bearer__call_invalid_token():
    token = authentication.generate_jwt(
        claims={"email": "test@test.com"},
    )
    request = RequestOutput({"Authorization": f"Bearer {token}"})
    with mock.patch.object(
        authentication.jwt,
        "decode",
        side_effect=ExpiredSignatureError,
    ):

        with pytest.raises(HTTPException):
            await authentication.JWTBearer().__call__(request)


@pytest.mark.anyio
async def test_jwt_bearer__call_invalid_authorization_code(get_fake_jwt):
    request = RequestOutput({"Authorization": f"test {get_fake_jwt}"})
    with pytest.raises(HTTPException):
        await authentication.JWTBearer(auto_error=False).__call__(request)


@pytest.mark.parametrize(
    ("use_fake_jwt", "expected"),
    (
        (True, True),
        (False, False),
    ),
)
def test_jwt_bearer_verify_jwt(use_fake_jwt, expected, get_fake_jwt):
    token = (
        get_fake_jwt
        if use_fake_jwt
        else authentication.generate_jwt(
            claims={"email": "test@test.com"},
        )
    )
    if use_fake_jwt:
        assert authentication.JWTBearer().verify_jwt(token) == expected
    else:
        with mock.patch.object(
            authentication.jwt,
            "decode",
            side_effect=ExpiredSignatureError,
        ):
            assert authentication.JWTBearer().verify_jwt(token) == expected
