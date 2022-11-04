from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationSpellModel


class ListVocationSpellSchema(
    sqlalchemy_to_pydantic(VocationSpellModel),  # type: ignore
):
    pass


class UpdateVocationSpellSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        VocationSpellModel,
        config=None,
    ),
):
    pass


class CreateVocationSpellSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        VocationSpellModel,
        config=None,
    ),
):
    pass
