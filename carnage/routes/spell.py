from fastapi import APIRouter

from carnage.database.repository.spell import SpellRepository
from carnage.routes.schemas.spell import (
    CreateSpellSchema,
    ListSpellSchema,
    UpdateSpellSchema,
)

router = APIRouter(prefix="/spell", tags=["spell"])
repository = SpellRepository()


@router.get("/", response_model=list[ListSpellSchema])
async def get() -> list[ListSpellSchema]:
    result = repository.select()
    return [ListSpellSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListSpellSchema)
async def get_by_id(identifier: str) -> ListSpellSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListSpellSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateSpellSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateSpellSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
