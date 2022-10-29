from typing import Type

from carnage.database.repository.map_schema import MapSchemaRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.map_schema import (
    CreateMapSchemaSchema,
    ListMapSchemaSchema,
    UpdateMapSchemaSchema,
)


class MapSchemaRoute(BaseRoute):
    def __init__(
        self,
        name: str = "map_schema",
        tags: list[str] = ["map", "map_schema"],
        repository: Type[MapSchemaRepository] = MapSchemaRepository,
        get_response_model: Type[ListMapSchemaSchema] = ListMapSchemaSchema,
        post_response_model: Type[
            CreateMapSchemaSchema
        ] = CreateMapSchemaSchema,
        put_response_model: Type[
            UpdateMapSchemaSchema
        ] = UpdateMapSchemaSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


map_schema_route = MapSchemaRoute()
