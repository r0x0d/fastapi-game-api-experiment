from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.race import RaceModel

ListRaceSchema = sqlalchemy_to_pydantic(RaceModel)
UpdateRaceSchema = sqlalchemy_to_pydantic(RaceModel, config=None)
CreateRaceSchema = sqlalchemy_to_pydantic(RaceModel, config=None)
