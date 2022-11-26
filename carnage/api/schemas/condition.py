from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.condition import ConditionModel


class ListConditionSchema(
    sqlalchemy_to_pydantic(ConditionModel),  # type: ignore
):
    pass


class UpdateConditionSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ConditionModel,
        config=None,
    ),
):
    pass


class CreateConditionSchema(
    sqlalchemy_to_pydantic(  # type: ignore
        ConditionModel,
        config=None,
    ),
):
    pass
