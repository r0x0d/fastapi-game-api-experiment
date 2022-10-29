from typing import Type

from carnage.database.repository.map_difficulty import MapDifficultyRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.map_difficulty import (
    CreateMapDifficultySchema,
    ListMapDifficultySchema,
    UpdateMapDifficultySchema,
)


class MapDifficultyRoute(BaseRoute):
    def __init__(
        self,
        name: str = "map_difficulty",
        tags: list[str] = ["map", "map_difficulty"],
        repository: Type[MapDifficultyRepository] = MapDifficultyRepository,
        get_response_model: Type[
            ListMapDifficultySchema
        ] = ListMapDifficultySchema,
        post_response_model: Type[
            CreateMapDifficultySchema
        ] = CreateMapDifficultySchema,
        put_response_model: Type[
            UpdateMapDifficultySchema
        ] = UpdateMapDifficultySchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


map_difficulty_route = MapDifficultyRoute()
