from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellModel

ListSpellSchema = sqlalchemy_to_pydantic(SpellModel)
UpdateSpellSchema = sqlalchemy_to_pydantic(SpellModel, config=None)
CreateSpellSchema = sqlalchemy_to_pydantic(SpellModel, config=None)
