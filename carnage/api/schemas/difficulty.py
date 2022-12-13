from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.difficulty import DifficultyModel


class ListDifficultySchema(
    sqlalchemy_to_pydantic(DifficultyModel),  # type: ignore
):
    pass


class UpdateDifficultySchema(
    sqlalchemy_to_pydantic(DifficultyModel, config=None),  # type: ignore
):
    pass


class CreateDifficultySchema(
    sqlalchemy_to_pydantic(DifficultyModel, config=None),  # type: ignore
):
    pass
