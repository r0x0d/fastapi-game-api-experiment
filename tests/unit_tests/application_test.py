from fastapi import FastAPI

from carnage import application


def test_create_app():
    assert isinstance(application.create_app(), FastAPI)
