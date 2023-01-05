from typing import Type

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from carnage.api.auth.authentication import APIJWTBearer
from carnage.database.repository.base import BaseRepository


class BaseRoute:
    list_schema = BaseModel
    create_schema = BaseModel
    update_schema = BaseModel

    def __init__(
        self,
        name: str = "base",
        tags: list[str] = ["base"],
        repository: Type[BaseRepository] = BaseRepository,
        dependencies: list[Depends] = [Depends(APIJWTBearer())],
    ) -> None:
        """Base constructor for all API routes.

        In the base class we define how the routes should look like and the
        methods that are associated with each endpoint. Those methods can (and
        are) overriden in each class that inherits from this base.

        :param name: The name of the route.
        :param tags: Tags associated with the route.
        :param repository: The repository that is used in queries.
        :param dependencies: List of dependencies for the routes.
        """
        self.name = name
        self.repository = repository()
        self.router = APIRouter(
            prefix=f"/{name}",
            tags=tags,
            dependencies=dependencies,
        )
        self.router.add_api_route(
            "/",
            self.get,
            methods=["GET"],
            status_code=200,
            response_model=list[self.list_schema],  # type: ignore
        )
        self.router.add_api_route(
            "/{identifier}",
            self.get_by_id,
            methods=["GET"],
            status_code=200,
            response_model=self.list_schema,
        )
        self.router.add_api_route(
            "/",
            self.post,
            methods=["POST"],
            status_code=201,
        )
        self.router.add_api_route(
            "/{identifier}",
            self.put,
            methods=["PUT", "PATCH"],
            status_code=204,
        )
        self.router.add_api_route(
            "/{identifier}",
            self.delete,
            methods=["DELETE"],
            status_code=204,
        )

    async def post(self, request: BaseModel) -> None:
        """Async method that represents a post request to this API.

        :param request: The data send throught the request.
        """
        self.repository.insert(values=request.dict())

    async def get(self) -> list[BaseModel]:
        """Async method that represents a normal get request to this API."""
        result = self.repository.select()
        return [self.list_schema.from_orm(item) for item in result]

    async def get_by_id(self, identifier: str) -> BaseModel:
        """Async method that represents a normal get to this API.

        This instance of get request is meant to be used with an identifier to
        filter for a specific result.

        :param identifier: The unique identifier used in the query.
        """
        result = self.repository.select_by_id(identifier=identifier)
        return self.list_schema.from_orm(result[0])

    async def put(self, request: BaseModel, identifier: str) -> None:
        """Async method that update data for this API.

        :param request: The data send throught the request.
        :param identifier: The unique identifier used in the query.
        """
        self.repository.update(values=request.dict(), identifier=identifier)

    async def delete(self, identifier: str) -> None:
        """Async method that deletes an entry for this API.

        :param identifier: The unique identifier used in the query.
        """
        self.repository.delete(identifier=identifier)
