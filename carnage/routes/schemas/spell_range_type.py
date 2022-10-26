from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell_range_type import SpellRangeTypeModel

ListSpellRangeTypeSchema = sqlalchemy_to_pydantic(SpellRangeTypeModel)
UpdateSpellRangeTypeSchema = sqlalchemy_to_pydantic(
    SpellRangeTypeModel,
    config=None,
)
CreateSpellRangeTypeSchema = sqlalchemy_to_pydantic(
    SpellRangeTypeModel,
    config=None,
)
