from typing import Type

from carnage.database.repository.size import SizeRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.size import (
    CreateSizeSchema,
    ListSizeSchema,
    UpdateSizeSchema,
)


class SizeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "size",
        tags: list[str] = ["size"],
        repository: Type[SizeRepository] = SizeRepository,
        get_response_model: Type[ListSizeSchema] = ListSizeSchema,
        post_response_model: Type[CreateSizeSchema] = CreateSizeSchema,
        put_response_model: Type[UpdateSizeSchema] = UpdateSizeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


size_route = SizeRoute()
