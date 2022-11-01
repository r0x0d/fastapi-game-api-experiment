from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.aligment import AligmentModel
from carnage.database.repository.aligment import AligmentRepository
from carnage.routes.base import BaseRoute


class ListAligmentSchema(
    sqlalchemy_to_pydantic(AligmentModel),  # type: ignore
):
    pass


class UpdateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    pass


class CreateAligmentSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        AligmentModel,
        config=None,
    ),
):
    pass


class AligmentRoute(BaseRoute):
    list_schema = ListAligmentSchema
    create_schema = CreateAligmentSchema
    update_schema = UpdateAligmentSchema

    def __init__(
        self,
        name: str = "aligment",
        tags: list[str] = ["aligment"],
        repository: Type[AligmentRepository] = AligmentRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListAligmentSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListAligmentSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateAligmentSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateAligmentSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = AligmentRoute()
