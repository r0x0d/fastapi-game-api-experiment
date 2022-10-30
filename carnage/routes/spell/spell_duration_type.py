from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellDurationTypeModel
from carnage.database.repository.spell import SpellDurationTypeRepository
from carnage.routes.base import BaseRoute

ListSpellDurationTypeSchema = sqlalchemy_to_pydantic(SpellDurationTypeModel)
UpdateSpellDurationTypeSchema = sqlalchemy_to_pydantic(
    SpellDurationTypeModel,
    config=None,
)
CreateSpellDurationTypeSchema = sqlalchemy_to_pydantic(
    SpellDurationTypeModel,
    config=None,
)


class SpellDurationTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell_duration_type",
        tags: list[str] = ["spell", "spell-duration-type"],
        repository: Type[
            SpellDurationTypeRepository
        ] = SpellDurationTypeRepository,
        get_response_model: BaseModel = ListSpellDurationTypeSchema,
        post_response_model: BaseModel = CreateSpellDurationTypeSchema,
        put_response_model: BaseModel = UpdateSpellDurationTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = SpellDurationTypeRoute()
