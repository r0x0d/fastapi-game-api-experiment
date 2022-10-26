from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell_school import SpellSchoolModel

ListSpellSchoolSchema = sqlalchemy_to_pydantic(SpellSchoolModel)
UpdateSpellSchoolSchema = sqlalchemy_to_pydantic(SpellSchoolModel, config=None)
CreateSpellSchoolSchema = sqlalchemy_to_pydantic(SpellSchoolModel, config=None)
