from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.dungeon import DungeonDifficultyModel


class ListDungeonDifficultySchema(
    sqlalchemy_to_pydantic(DungeonDifficultyModel),  # type: ignore
):
    pass


class UpdateDungeonDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonDifficultyModel,
        config=None,
    ),
):
    pass


class CreateDungeonDifficultySchema(
    sqlalchemy_to_pydantic(  # type: ignore
        DungeonDifficultyModel,
        config=None,
    ),
):
    pass
