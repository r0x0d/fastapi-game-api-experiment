from fastapi import APIRouter

from carnage.database.repository.spell_school import SpellSchoolRepository
from carnage.routes.schemas.spell_school import (
    CreateSpellSchoolSchema,
    ListSpellSchoolSchema,
    UpdateSpellSchoolSchema,
)

router = APIRouter(prefix="/spell_school", tags=["spell-school"])
repository = SpellSchoolRepository()


@router.get("/", response_model=list[ListSpellSchoolSchema])
async def get() -> list[ListSpellSchoolSchema]:
    result = repository.select()
    return [ListSpellSchoolSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListSpellSchoolSchema)
async def get_by_id(identifier: str) -> ListSpellSchoolSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListSpellSchoolSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateSpellSchoolSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateSpellSchoolSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
