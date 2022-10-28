from typing import Type

from carnage.database.repository.vocation import VocationRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.vocation import (
    CreateVocationSchema,
    ListVocationSchema,
    UpdateVocationSchema,
)


class VocationRoute(BaseRoute):
    def __init__(
        self,
        name: str = "vocation",
        tags: list[str] = ["vocation"],
        repository: Type[VocationRepository] = VocationRepository,
        get_response_model: Type[ListVocationSchema] = ListVocationSchema,
        post_response_model: Type[CreateVocationSchema] = CreateVocationSchema,
        put_response_model: Type[UpdateVocationSchema] = UpdateVocationSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


vocation_route = VocationRoute()
