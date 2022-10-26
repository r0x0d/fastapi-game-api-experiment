from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell_duration_type import SpellDurationTypeModel

ListSpellDurationTypeSchema = sqlalchemy_to_pydantic(SpellDurationTypeModel)
UpdateSpellDurationTypeSchema = sqlalchemy_to_pydantic(
    SpellDurationTypeModel,
    config=None,
)
CreateSpellDurationTypeSchema = sqlalchemy_to_pydantic(
    SpellDurationTypeModel,
    config=None,
)
