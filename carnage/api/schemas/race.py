from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from carnage.database.models.race import RaceModel


class ListRaceSchema(
    sqlalchemy_to_pydantic(RaceModel),  # type: ignore
):
    pass


class UpdateRaceSchema(
    sqlalchemy_to_pydantic(RaceModel, config=None),  # type: ignore
):
    pass


class CreateRaceSchema(
    sqlalchemy_to_pydantic(RaceModel, config=None),  # type: ignore
):
    pass
