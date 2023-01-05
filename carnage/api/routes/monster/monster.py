from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.monster import (
    CreateMonsterSchema,
    ListMonsterSchema,
    UpdateMonsterSchema,
)
from carnage.database.repository.monster import MonsterRepository


class MonsterRoute(BaseRoute):
    list_schema = ListMonsterSchema
    create_schema = CreateMonsterSchema
    update_schema = UpdateMonsterSchema

    def __init__(
        self,
        name: str = "monster",
        tags: list[str] = ["monster"],
        repository: Type[MonsterRepository] = MonsterRepository,
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

    async def post(self, request: CreateMonsterSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListMonsterSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMonsterSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(self, request: UpdateMonsterSchema, identifier: str) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = MonsterRoute()
