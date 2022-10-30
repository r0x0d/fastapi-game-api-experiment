from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.size import SizeModel
from carnage.database.repository.size import SizeRepository
from carnage.routes.base import BaseRoute

ListSizeSchema = sqlalchemy_to_pydantic(SizeModel)
UpdateSizeSchema = sqlalchemy_to_pydantic(SizeModel, config=None)
CreateSizeSchema = sqlalchemy_to_pydantic(SizeModel, config=None)


class SizeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "size",
        tags: list[str] = ["size"],
        repository: Type[SizeRepository] = SizeRepository,
        get_response_model: BaseModel = ListSizeSchema,
        post_response_model: BaseModel = CreateSizeSchema,
        put_response_model: BaseModel = UpdateSizeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = SizeRoute()
