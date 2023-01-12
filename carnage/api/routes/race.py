from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.race import (
    CreateRaceSchema,
    ListRaceSchema,
    UpdateRaceSchema,
)
from carnage.database.repository.race import RaceRepository


class RaceRoute(BaseRoute):
    list_schema = ListRaceSchema
    update_schema = CreateRaceSchema
    create_schema = UpdateRaceSchema

    def __init__(
        self,
        name: str = "race",
        tags: list[str] = ["race"],
        repository: type[RaceRepository] = RaceRepository,
    ) -> None:
        """Constructor for HTTP API route.

        :param name: The name of the route
        :param tags: List of tags associated with the route
        :param repository: The repository that may be used to query
            information.
        """
        super().__init__(
            name=name,
            tags=tags,
            repository=repository,
        )

    async def post(self, request: CreateRaceSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListRaceSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListRaceSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(self, request: UpdateRaceSchema, identifier: str) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = RaceRoute()
