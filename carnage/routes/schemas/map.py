from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.map import MapModel

ListMapSchema = sqlalchemy_to_pydantic(MapModel)
UpdateMapSchema = sqlalchemy_to_pydantic(MapModel, config=None)
CreateMapSchema = sqlalchemy_to_pydantic(MapModel, config=None)
