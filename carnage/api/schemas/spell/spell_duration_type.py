from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellDurationTypeModel


class ListSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(SpellDurationTypeModel),  # type: ignore
):
    pass


class UpdateSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellDurationTypeModel,
        config=None,
    ),
):
    pass


class CreateSpellDurationTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellDurationTypeModel,
        config=None,
    ),
):
    pass
