from fastapi import APIRouter

from carnage.database.repository.spell_duration_type import (
    SpellDurationTypeRepository,
)
from carnage.routes.schemas.spell_duration_type import (
    CreateSpellDurationTypeSchema,
    ListSpellDurationTypeSchema,
    UpdateSpellDurationTypeSchema,
)

router = APIRouter(prefix="/spell_duration_type", tags=["spell-duration-type"])
repository = SpellDurationTypeRepository()


@router.get("/", response_model=list[ListSpellDurationTypeSchema])
async def get() -> list[ListSpellDurationTypeSchema]:
    result = repository.select()
    return [ListSpellDurationTypeSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListSpellDurationTypeSchema)
async def get_by_id(identifier: str) -> ListSpellDurationTypeSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListSpellDurationTypeSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateSpellDurationTypeSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateSpellDurationTypeSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
