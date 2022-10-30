from typing import Type

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationSpellModel
from carnage.database.repository.vocation import VocationSpellRepository
from carnage.routes.base import BaseRoute

ListVocationSpellSchema = sqlalchemy_to_pydantic(VocationSpellModel)
UpdateVocationSpellSchema = sqlalchemy_to_pydantic(
    VocationSpellModel,
    config=None,
)
CreateVocationSpellSchema = sqlalchemy_to_pydantic(
    VocationSpellModel,
    config=None,
)


class VocationSpellRoute(BaseRoute):
    def __init__(
        self,
        name: str = "vocation_spell",
        tags: list[str] = ["vocation", "vocation-spell"],
        repository: Type[VocationSpellRepository] = VocationSpellRepository,
        get_response_model: BaseModel = ListVocationSpellSchema,
        post_response_model: BaseModel = CreateVocationSpellSchema,
        put_response_model: BaseModel = UpdateVocationSpellSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


route = VocationSpellRoute()
