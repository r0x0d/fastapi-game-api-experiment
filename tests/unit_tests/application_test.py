from carnage import application
from fastapi import FastAPI


def test_create_app():
    assert isinstance(application.create_app(), FastAPI)
