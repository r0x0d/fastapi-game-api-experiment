from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellSchoolModel


class ListSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel),  # type: ignore
):
    pass


class UpdateSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel, config=None),  # type: ignore
):
    pass


class CreateSpellSchoolSchema(
    sqlalchemy_to_pydantic(SpellSchoolModel, config=None),  # type: ignore
):
    pass
