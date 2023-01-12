from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.spell import (
    CreateSpellSchema,
    ListSpellSchema,
    UpdateSpellSchema,
)
from carnage.database.repository.spell import SpellRepository


class SpellRoute(BaseRoute):
    list_schema = ListSpellSchema
    create_schema = CreateSpellSchema
    update_schema = UpdateSpellSchema

    def __init__(
        self,
        name: str = "spell",
        tags: list[str] = ["spell"],
        repository: type[SpellRepository] = SpellRepository,
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

    async def post(self, request: CreateSpellSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListSpellSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(self, request: UpdateSpellSchema, identifier: str) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = SpellRoute()
