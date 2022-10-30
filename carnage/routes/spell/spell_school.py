from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellSchoolModel
from carnage.database.repository.spell import SpellSchoolRepository
from carnage.routes.base import BaseRoute

ListSpellSchoolSchema = sqlalchemy_to_pydantic(SpellSchoolModel)
UpdateSpellSchoolSchema = sqlalchemy_to_pydantic(SpellSchoolModel, config=None)
CreateSpellSchoolSchema = sqlalchemy_to_pydantic(SpellSchoolModel, config=None)


class SpellSchoolRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell_school",
        tags: list[str] = ["spell", "spell-school"],
        repository: Type[SpellSchoolRepository] = SpellSchoolRepository,
        get_response_model: BaseModel = ListSpellSchoolSchema,
        post_response_model: BaseModel = CreateSpellSchoolSchema,
        put_response_model: BaseModel = UpdateSpellSchoolSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = SpellSchoolRoute()
