"""Module that implements the Dungeon Route."""

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.dungeon import (
    CreateDungeonSchema,
    ListDungeonSchema,
    UpdateDungeonSchema,
)
from carnage.database.repository.dungeon import DungeonRepository


class DungeonRoute(BaseRoute):
    """Class that overrides the base routes for an API request."""

    list_schema = ListDungeonSchema
    create_schema = CreateDungeonSchema
    update_schema = UpdateDungeonSchema

    def __init__(
        self,
        name: str = "dungeon",
        tags: list[str] = ["dungeon"],
        repository: type[DungeonRepository] = DungeonRepository,
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

    async def post(self, request: CreateDungeonSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListDungeonSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListDungeonSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(self, request: UpdateDungeonSchema, identifier: str) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = DungeonRoute()
