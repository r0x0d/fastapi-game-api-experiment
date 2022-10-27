from typing import Type

from fastapi import APIRouter
from pydantic import BaseModel

from carnage.database.repository.base import BaseRepository


class BaseRoute:
    def __init__(
        self,
        name: str = "base",
        tags: list[str] = ["base"],
        repository: Type[BaseRepository] = BaseRepository,
        get_response_model: Type[BaseModel] = BaseModel,
        post_request_model: Type[BaseModel] = BaseModel,
        put_request_model: Type[BaseModel] = BaseModel,
    ) -> None:
        self.repository = repository()
        self.get_response_model = get_response_model
        self.post_request_model = post_request_model
        self.put_request_model = put_request_model
        self.router = APIRouter(prefix=f"/{name}", tags=tags)
        self.router.add_api_route(
            "/",
            self.get,
            methods=["GET"],
            status_code=200,
            response_model=list[get_response_model],  # type: ignore
        )
        self.router.add_api_route(
            "/{identifier}",
            self.get_by_id,
            methods=["GET"],
            status_code=200,
            response_model=get_response_model,
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

        # Updating the type annotations for both `post` and `put` as we can't
        # use `self.x` as a type annotation,
        self.post.__annotations__.update({"request": self.post_request_model})
        self.put.__annotations__.update({"request": self.put_request_model})

    async def get(self) -> list[BaseModel]:
        result = self.repository.select()
        return [self.get_response_model.from_orm(item) for item in result]

    async def get_by_id(self, identifier: str) -> BaseModel:
        result = self.repository.select_by_id(identifier=identifier)
        return self.get_response_model.from_orm(result[0])

    async def post(self, request: BaseModel) -> None:
        self.repository.insert(values=request.dict())

    async def put(
        self,
        request: BaseModel,
        identifier: str,
    ) -> None:
        self.repository.update(values=request.dict(), identifier=identifier)

    async def delete(self, identifier: str) -> None:
        self.repository.delete(identifier=identifier)
