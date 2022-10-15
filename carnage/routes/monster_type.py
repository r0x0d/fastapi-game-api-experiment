from fastapi import APIRouter

from carnage.database.repository.monster_type import MonsterTypeRepository
from carnage.routes.schemas.monster_type import (
    CreateMonsterTypeSchema,
    ListMonsterTypeSchema,
    UpdateMonsterTypeSchema,
)

router = APIRouter(prefix="/monster_type", tags=["monster-type"])
repository = MonsterTypeRepository()


@router.get("/", response_model=list[ListMonsterTypeSchema])
async def get() -> list[ListMonsterTypeSchema]:
    result = repository.select()
    return [ListMonsterTypeSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListMonsterTypeSchema)
async def get_by_id(identifier: str) -> ListMonsterTypeSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListMonsterTypeSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateMonsterTypeSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateMonsterTypeSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
