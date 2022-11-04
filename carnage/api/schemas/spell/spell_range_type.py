from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.spell import SpellRangeTypeModel


class ListSpellRangeTypeSchema(
    sqlalchemy_to_pydantic(SpellRangeTypeModel),  # type: ignore
):
    pass


class UpdateSpellRangeTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellRangeTypeModel,
        config=None,
    ),
):
    pass


class CreateSpellRangeTypeSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        SpellRangeTypeModel,
        config=None,
    ),
):
    pass
