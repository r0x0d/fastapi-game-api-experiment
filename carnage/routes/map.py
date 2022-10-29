from typing import Type

from carnage.database.repository.map import MapRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.map import (
    CreateMapSchema,
    ListMapSchema,
    UpdateMapSchema,
)


class MapRoute(BaseRoute):
    def __init__(
        self,
        name: str = "map",
        tags: list[str] = ["map"],
        repository: Type[MapRepository] = MapRepository,
        get_response_model: Type[ListMapSchema] = ListMapSchema,
        post_response_model: Type[CreateMapSchema] = CreateMapSchema,
        put_response_model: Type[UpdateMapSchema] = UpdateMapSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


map_route = MapRoute()
