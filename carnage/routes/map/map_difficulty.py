from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.map import MapDifficultyModel
from carnage.database.repository.map import MapDifficultyRepository
from carnage.routes.base import BaseRoute

ListMapDifficultySchema = sqlalchemy_to_pydantic(MapDifficultyModel)
UpdateMapDifficultySchema = sqlalchemy_to_pydantic(
    MapDifficultyModel,
    config=None,
)
CreateMapDifficultySchema = sqlalchemy_to_pydantic(
    MapDifficultyModel,
    config=None,
)


class MapDifficultyRoute(BaseRoute):
    def __init__(
        self,
        name: str = "map_difficulty",
        tags: list[str] = ["map", "map_difficulty"],
        repository: Type[MapDifficultyRepository] = MapDifficultyRepository,
        get_response_model: BaseModel = ListMapDifficultySchema,
        post_response_model: BaseModel = CreateMapDifficultySchema,
        put_response_model: BaseModel = UpdateMapDifficultySchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = MapDifficultyRoute()
