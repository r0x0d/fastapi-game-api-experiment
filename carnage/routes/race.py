from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.race import RaceModel
from carnage.database.repository.race import RaceRepository
from carnage.routes.base import BaseRoute

ListRaceSchema = sqlalchemy_to_pydantic(RaceModel)
UpdateRaceSchema = sqlalchemy_to_pydantic(RaceModel, config=None)
CreateRaceSchema = sqlalchemy_to_pydantic(RaceModel, config=None)


class RaceRoute(BaseRoute):
    def __init__(
        self,
        name: str = "race",
        tags: list[str] = ["race"],
        repository: Type[RaceRepository] = RaceRepository,
        get_response_model: BaseModel = ListRaceSchema,
        post_response_model: BaseModel = CreateRaceSchema,
        put_response_model: BaseModel = UpdateRaceSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = RaceRoute()
