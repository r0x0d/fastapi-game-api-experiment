from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.map import MapModel
from carnage.database.repository.map import MapRepository
from carnage.routes.base import BaseRoute

ListMapSchema = sqlalchemy_to_pydantic(MapModel)
UpdateMapSchema = sqlalchemy_to_pydantic(MapModel, config=None)
CreateMapSchema = sqlalchemy_to_pydantic(MapModel, config=None)


class MapRoute(BaseRoute):
    def __init__(
        self,
        name: str = "map",
        tags: list[str] = ["map"],
        repository: Type[MapRepository] = MapRepository,
        get_response_model: BaseModel = ListMapSchema,
        post_response_model: BaseModel = CreateMapSchema,
        put_response_model: BaseModel = UpdateMapSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = MapRoute()
