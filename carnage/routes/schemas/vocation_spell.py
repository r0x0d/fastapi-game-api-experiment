from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation_spell import VocationSpellModel

ListVocationSpellSchema = sqlalchemy_to_pydantic(VocationSpellModel)
UpdateVocationSpellSchema = sqlalchemy_to_pydantic(
    VocationSpellModel,
    config=None,
)
CreateVocationSpellSchema = sqlalchemy_to_pydantic(
    VocationSpellModel,
    config=None,
)
