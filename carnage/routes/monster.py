from fastapi import APIRouter

from carnage.database.repository.monster import MonsterRepository
from carnage.routes.schemas.monster import (
    CreateMonsterSchema,
    ListMonsterSchema,
    UpdateMonsterSchema,
)

router = APIRouter(prefix="/monster", tags=["monster"])
repository = MonsterRepository()


@router.get("/", response_model=list[ListMonsterSchema])
async def get() -> list[ListMonsterSchema]:
    result = repository.select()
    return [ListMonsterSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListMonsterSchema)
async def get_by_id(identifier: str) -> ListMonsterSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListMonsterSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateMonsterSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateMonsterSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
