from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.aligment import AligmentModel
from carnage.database.repository.aligment import AligmentRepository
from carnage.routes.base import BaseRoute

ListAligmentSchema = sqlalchemy_to_pydantic(AligmentModel)
UpdateAligmentSchema = sqlalchemy_to_pydantic(
    AligmentModel,
    config=None,
)
CreateAligmentSchema = sqlalchemy_to_pydantic(
    AligmentModel,
    config=None,
)


class AligmentRoute(BaseRoute):
    def __init__(
        self,
        name: str = "aligment",
        tags: list[str] = ["aligment"],
        repository: Type[AligmentRepository] = AligmentRepository,
        get_response_model: BaseModel = ListAligmentSchema,
        post_response_model: BaseModel = CreateAligmentSchema,
        put_response_model: BaseModel = UpdateAligmentSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = AligmentRoute()
