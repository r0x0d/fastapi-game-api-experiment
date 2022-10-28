from collections import namedtuple
from unittest import mock

import pytest
from fastapi import FastAPI

from carnage import application

SettingOutput = namedtuple("SettingOutput", ("secret_key"))


def test_create_app(database_session_mock, monkeypatch):
    assert isinstance(application.create_app(), FastAPI)


@pytest.mark.parametrize(("development"), (("1"), ("")))
def test_add_middleware(development, database_session_mock, monkeypatch):
    with mock.patch.object(application, "DEVELOPMENT", development):
        application.add_middleware(FastAPI())
