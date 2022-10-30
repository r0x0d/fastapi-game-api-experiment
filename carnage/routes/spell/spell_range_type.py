from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellRangeTypeModel
from carnage.database.repository.spell import SpellRangeTypeRepository
from carnage.routes.base import BaseRoute

ListSpellRangeTypeSchema = sqlalchemy_to_pydantic(SpellRangeTypeModel)
UpdateSpellRangeTypeSchema = sqlalchemy_to_pydantic(
    SpellRangeTypeModel,
    config=None,
)
CreateSpellRangeTypeSchema = sqlalchemy_to_pydantic(
    SpellRangeTypeModel,
    config=None,
)


class SpellRangeTypeRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell_range_type",
        tags: list[str] = ["spell", "spell-range-type"],
        repository: Type[SpellRangeTypeRepository] = SpellRangeTypeRepository,
        get_response_model: BaseModel = ListSpellRangeTypeSchema,
        post_response_model: BaseModel = CreateSpellRangeTypeSchema,
        put_response_model: BaseModel = UpdateSpellRangeTypeSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = SpellRangeTypeRoute()
