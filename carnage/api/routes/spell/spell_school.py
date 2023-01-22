"""Module that implements the Spell School Route."""

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.spell import (
    CreateSpellSchoolSchema,
    ListSpellSchoolSchema,
    UpdateSpellSchoolSchema,
)
from carnage.database.repository.spell import SpellSchoolRepository


class SpellSchoolRoute(BaseRoute):
    """Class that overrides the base routes for an API request."""

    list_schema = ListSpellSchoolSchema
    create_schema = CreateSpellSchoolSchema
    update_schema = UpdateSpellSchoolSchema

    def __init__(
        self,
        name: str = "spell_school",
        tags: list[str] = ["spell", "spell-school"],
        repository: type[SpellSchoolRepository] = SpellSchoolRepository,
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

    async def post(self, request: CreateSpellSchoolSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListSpellSchoolSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellSchoolSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(
        self,
        request: UpdateSpellSchoolSchema,
        identifier: str,
    ) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = SpellSchoolRoute()
