from typing import Type

from carnage.database.repository.vocation_spell import VocationSpellRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.vocation_spell import (
    CreateVocationSpellSchema,
    ListVocationSpellSchema,
    UpdateVocationSpellSchema,
)


class VocationSpellRoute(BaseRoute):
    def __init__(
        self,
        name: str = "vocation_spell",
        tags: list[str] = ["vocation", "vocation-spell"],
        repository: Type[VocationSpellRepository] = VocationSpellRepository,
        get_response_model: Type[
            ListVocationSpellSchema
        ] = ListVocationSpellSchema,
        post_response_model: Type[
            CreateVocationSpellSchema
        ] = CreateVocationSpellSchema,
        put_response_model: Type[
            UpdateVocationSpellSchema
        ] = UpdateVocationSpellSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


vocation_spell_route = VocationSpellRoute()
