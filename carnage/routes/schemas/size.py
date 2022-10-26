from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.size import SizeModel

ListSizeSchema = sqlalchemy_to_pydantic(SizeModel)
UpdateSizeSchema = sqlalchemy_to_pydantic(SizeModel, config=None)
CreateSizeSchema = sqlalchemy_to_pydantic(SizeModel, config=None)
