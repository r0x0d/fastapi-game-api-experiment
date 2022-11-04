from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellModel


class ListSpellSchema(
    sqlalchemy_to_pydantic(SpellModel),  # type: ignore
):
    pass


class UpdateSpellSchema(
    sqlalchemy_to_pydantic(SpellModel, config=None),  # type: ignore
):
    pass


class CreateSpellSchema(
    sqlalchemy_to_pydantic(SpellModel, config=None),  # type: ignore
):
    pass
