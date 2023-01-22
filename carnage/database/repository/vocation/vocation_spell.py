"""Module that represents the Vocation Spell repository."""

from functools import lru_cache

from sqlalchemy import select

from carnage.database.models.vocation import VocationSpellModel
from carnage.database.repository.base import BaseRepository


class VocationSpellRepository(BaseRepository):
    """Class that overrides the base repository methods."""

    def __init__(
        self,
        model: type[VocationSpellModel] = VocationSpellModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)

    @lru_cache
    def select_by_spell_id(self, spell_id: str) -> VocationSpellModel:
        """Get results from database filtering by spell id.

        :param spell_id: Spell id to be used in the filter.
        """
        statement = select(self.model).where(
            self.model.spell_id == spell_id
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).first()
