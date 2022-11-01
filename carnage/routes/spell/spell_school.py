from typing import Type

from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellSchoolModel
from carnage.database.repository.spell import SpellSchoolRepository
from carnage.routes.base import BaseRoute


class ListSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel),  # type: ignore
):
    pass


class UpdateSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel, config=None),  # type: ignore
):
    pass


class CreateSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel, config=None),  # type: ignore
):
    pass


class SpellSchoolRoute(BaseRoute):
    list_schema = ListSpellSchoolSchema
    create_schema = CreateSpellSchoolSchema
    update_schema = UpdateSpellSchoolSchema

    def __init__(
        self,
        name: str = "spell_school",
        tags: list[str] = ["spell", "spell-school"],
        repository: Type[SpellSchoolRepository] = SpellSchoolRepository,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
        )

    async def get(self) -> list[ListSpellSchoolSchema]:
        return await super().get()

    async def get_by_id(self, identifier: str) -> ListSpellSchoolSchema:
        return await super().get_by_id(identifier)

    async def post(self, request: CreateSpellSchoolSchema) -> None:
        return await super().post(request)

    async def put(
        self,
        request: UpdateSpellSchoolSchema,
        identifier: str,
    ) -> None:
        return await super().put(request, identifier)


route = SpellSchoolRoute()
