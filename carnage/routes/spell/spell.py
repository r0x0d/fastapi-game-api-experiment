from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellModel
from carnage.database.repository.spell import SpellRepository
from carnage.routes.base import BaseRoute

ListSpellSchema = sqlalchemy_to_pydantic(SpellModel)
UpdateSpellSchema = sqlalchemy_to_pydantic(SpellModel, config=None)
CreateSpellSchema = sqlalchemy_to_pydantic(SpellModel, config=None)


class SpellRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell",
        tags: list[str] = ["spell"],
        repository: Type[SpellRepository] = SpellRepository,
        get_response_model: BaseModel = ListSpellSchema,
        post_response_model: BaseModel = CreateSpellSchema,
        put_response_model: BaseModel = UpdateSpellSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = SpellRoute()
