from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.aligment import AligmentModel

ListAligmentSchema = sqlalchemy_to_pydantic(AligmentModel)
UpdateAligmentSchema = sqlalchemy_to_pydantic(AligmentModel, config=None)
CreateAligmentSchema = sqlalchemy_to_pydantic(AligmentModel, config=None)
