from typing import Type

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.monster import (
    CreateMonsterTypeSchema,
    ListMonsterTypeSchema,
    UpdateMonsterTypeSchema,
)
from carnage.database.repository.monster.monster_type import (
    MonsterTypeRepository,
)


class MonsterTypeRoute(BaseRoute):
    list_schema = ListMonsterTypeSchema
    create_schema = CreateMonsterTypeSchema
    update_schema = UpdateMonsterTypeSchema

    def __init__(
        self,
        name: str = "monster_type",
        tags: list[str] = ["monster", "monster_type"],
        repository: Type[MonsterTypeRepository] = MonsterTypeRepository,
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

    async def post(self, request: CreateMonsterTypeSchema) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        return await super().post(request)

    async def get(self) -> list[ListMonsterTypeSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListMonsterTypeSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(
        self,
        request: UpdateMonsterTypeSchema,
        identifier: str,
    ) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = MonsterTypeRoute()
