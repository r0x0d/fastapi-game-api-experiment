from typing import Type

from fastapi import HTTPException, Request

from carnage.api.routes.base import BaseRoute
from carnage.api.schemas.account import ListAccountSchema, UpdateAccountSchema
from carnage.database.repository.account import AccountRepository


class AccountRoute(BaseRoute):
    list_schema = ListAccountSchema
    update_schema = UpdateAccountSchema

    def __init__(
        self,
        name: str = "account",
        tags: list[str] = ["account"],
        repository: Type[AccountRepository] = AccountRepository,
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

    async def post(self, _: Request) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        raise HTTPException(
            status_code=418,
            detail="I can't do anything. I'm a teapot.",
        )

    async def get(self) -> list[ListAccountSchema]:
        """Async method that represents a normal get request to this API."""
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListAccountSchema:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        return await super().get_by_id(identifier)

    async def put(self, request: UpdateAccountSchema, identifier: str) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        return await super().put(request, identifier)


route = AccountRoute()
