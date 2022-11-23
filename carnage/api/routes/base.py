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

    async def get(self) -> list[BaseModel]:
        result = self.repository.select()
        return [self.list_schema.from_orm(item) for item in result]

    async def get_by_id(self, identifier: str) -> BaseModel:
        result = self.repository.select_by_id(identifier=identifier)
        return self.list_schema.from_orm(result[0])

    async def post(self, request: BaseModel) -> None:
        self.repository.insert(values=request.dict())

    async def put(self, request: BaseModel, identifier: str) -> None:
        self.repository.update(values=request.dict(), identifier=identifier)

    async def delete(self, identifier: str) -> None:
        self.repository.delete(identifier=identifier)
