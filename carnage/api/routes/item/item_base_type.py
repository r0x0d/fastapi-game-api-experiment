"""Module that implements the Item Base Type Route."""

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.item import (
    CreateItemBaseTypeSchema,
    ListItemBaseTypeSchema,
    UpdateItemBaseTypeSchema,
)
from carnage.database.repository.item import ItemBaseTypeRepository


class ItemBaseTypeRoute(BaseRoute):
    """Class that overrides the base routes for an API request."""

    list_schema = ListItemBaseTypeSchema
    create_schema = CreateItemBaseTypeSchema
    update_schema = UpdateItemBaseTypeSchema

    def __init__(
        self,
        name: str = "item_base_type",
        tags: list[str] = ["item", "item-base-type"],
        repository: type[ItemBaseTypeRepository] = ItemBaseTypeRepository,
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

    async def post(self, request: CreateItemBaseTypeSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListItemBaseTypeSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListItemBaseTypeSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(
        self,
        request: UpdateItemBaseTypeSchema,
        identifier: str,
    ) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = ItemBaseTypeRoute()
