from typing import Type

from carnage.database.repository.aligment import AligmentRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.aligment import (
    CreateAligmentSchema,
    ListAligmentSchema,
    UpdateAligmentSchema,
)


class AligmentRoute(BaseRoute):
    def __init__(
        self,
        name: str = "aligment",
        tags: list[str] = ["aligment"],
        repository: Type[AligmentRepository] = AligmentRepository,
        get_response_model: Type[ListAligmentSchema] = ListAligmentSchema,
        post_response_model: Type[CreateAligmentSchema] = CreateAligmentSchema,
        put_response_model: Type[UpdateAligmentSchema] = UpdateAligmentSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


aligment_route = AligmentRoute()
