from collections import namedtuple
from unittest import mock

import pytest
from fastapi import FastAPI

from carnage import application

SettingOutput = namedtuple("SettingOutput", ("secret_key"))


def test_create_app(database_session_mock):
    assert isinstance(application.create_app(), FastAPI)


@pytest.mark.parametrize(("development"), (("development"), ("production")))
def test_add_router(development, database_session_mock):
    with mock.patch.object(application, "CARNAGE_ENVIRONMENT", development):
        application.add_router(FastAPI())


@pytest.mark.parametrize(("development"), (("development"), ("production")))
def test_add_middleware(development, database_session_mock):
    with mock.patch.object(application, "CARNAGE_ENVIRONMENT", development):
        application.add_middleware(FastAPI())
