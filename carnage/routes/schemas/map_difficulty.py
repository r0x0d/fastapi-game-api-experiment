from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.map_difficulty import MapDifficultyModel

ListMapDifficultySchema = sqlalchemy_to_pydantic(MapDifficultyModel)
UpdateMapDifficultySchema = sqlalchemy_to_pydantic(
    MapDifficultyModel,
    config=None,
)
CreateMapDifficultySchema = sqlalchemy_to_pydantic(
    MapDifficultyModel,
    config=None,
)
