"""Module that implements the Condition Route."""

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.condition import (
    CreateConditionSchema,
    ListConditionSchema,
    UpdateConditionSchema,
)
from carnage.database.repository.condition import ConditionRepository


class ConditionRoute(BaseRoute):
    """Class that overrides the base routes for an API request."""

    list_schema = ListConditionSchema
    create_schema = CreateConditionSchema
    update_schema = UpdateConditionSchema

    def __init__(
        self,
        name: str = "condition",
        tags: list[str] = ["condition"],
        repository: type[ConditionRepository] = ConditionRepository,
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

    async def post(self, request: CreateConditionSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListConditionSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListConditionSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(
        self,
        request: UpdateConditionSchema,
        identifier: str,
    ) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = ConditionRoute()
