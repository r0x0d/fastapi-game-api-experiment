from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellDurationTypeModel
from carnage.database.repository.spell import SpellDurationTypeRepository
from carnage.routes.base import BaseRoute


class ListSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(SpellDurationTypeModel),  # type: ignore
):
    pass


class UpdateSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellDurationTypeModel,
        config=None,
    ),
):
    pass


class CreateSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellDurationTypeModel,
        config=None,
    ),
):
    pass


class SpellDurationTypeRoute(BaseRoute):
    list_schema = ListSpellDurationTypeSchema
    create_schema = CreateSpellDurationTypeSchema
    update_schema = UpdateSpellDurationTypeSchema

    def __init__(
        self,
        name: str = "spell_duration_type",
        tags: list[str] = ["spell", "spell-duration-type"],
        repository: Type[
            SpellDurationTypeRepository
        ] = SpellDurationTypeRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListSpellDurationTypeSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellDurationTypeSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSpellDurationTypeSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateSpellDurationTypeSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = SpellDurationTypeRoute()
