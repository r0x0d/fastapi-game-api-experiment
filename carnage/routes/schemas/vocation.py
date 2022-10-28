from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.vocation import VocationModel

ListVocationSchema = sqlalchemy_to_pydantic(VocationModel)
UpdateVocationSchema = sqlalchemy_to_pydantic(VocationModel, config=None)
CreateVocationSchema = sqlalchemy_to_pydantic(VocationModel, config=None)
