from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationModel
from carnage.database.repository.vocation import VocationRepository
from carnage.routes.base import BaseRoute

ListVocationSchema = sqlalchemy_to_pydantic(VocationModel)
UpdateVocationSchema = sqlalchemy_to_pydantic(VocationModel, config=None)
CreateVocationSchema = sqlalchemy_to_pydantic(VocationModel, config=None)


class VocationRoute(BaseRoute):
    def __init__(
        self,
        name: str = "vocation",
        tags: list[str] = ["vocation"],
        repository: Type[VocationRepository] = VocationRepository,
        get_response_model: BaseModel = ListVocationSchema,
        post_response_model: BaseModel = CreateVocationSchema,
        put_response_model: BaseModel = UpdateVocationSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = VocationRoute()
