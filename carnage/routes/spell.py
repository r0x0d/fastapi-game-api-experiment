from typing import Type

from carnage.database.repository.spell import SpellRepository
from carnage.routes.base import BaseRoute
from carnage.routes.schemas.spell import (
    CreateSpellSchema,
    ListSpellSchema,
    UpdateSpellSchema,
)


class SpellRoute(BaseRoute):
    def __init__(
        self,
        name: str = "spell",
        tags: list[str] = ["spell"],
        repository: Type[SpellRepository] = SpellRepository,
        get_response_model: Type[ListSpellSchema] = ListSpellSchema,
        post_response_model: Type[CreateSpellSchema] = CreateSpellSchema,
        put_response_model: Type[UpdateSpellSchema] = UpdateSpellSchema,
    ) -> None:
        super().__init__(
            name,
            tags,
            repository,
            get_response_model,
            post_response_model,
            put_response_model,
        )


spell_route = SpellRoute()
