from typing import Type

from carnage.database.repository.race import RaceRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.race import (
    CreateRaceSchema,
    ListRaceSchema,
    UpdateRaceSchema,
)


class RaceRoute(BaseRoute):
    def __init__(
        self,
        name: str = "race",
        tags: list[str] = ["race"],
        repository: Type[RaceRepository] = RaceRepository,
        get_response_model: Type[ListRaceSchema] = ListRaceSchema,
        post_response_model: Type[CreateRaceSchema] = CreateRaceSchema,
        put_response_model: Type[UpdateRaceSchema] = UpdateRaceSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


race_route = RaceRoute()
