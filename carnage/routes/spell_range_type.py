from fastapi import APIRouter

from carnage.database.repository.spell_range_type import (
    SpellRangeTypeRepository,
)
from carnage.routes.schemas.spell_range_type import (
    CreateSpellRangeTypeSchema,
    ListSpellRangeTypeSchema,
    UpdateSpellRangeTypeSchema,
)

router = APIRouter(prefix="/spell_range_type", tags=["spell-range-type"])
repository = SpellRangeTypeRepository()


@router.get("/", response_model=list[ListSpellRangeTypeSchema])
async def get() -> list[ListSpellRangeTypeSchema]:
    result = repository.select()
    return [ListSpellRangeTypeSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListSpellRangeTypeSchema)
async def get_by_id(identifier: str) -> ListSpellRangeTypeSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListSpellRangeTypeSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateSpellRangeTypeSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateSpellRangeTypeSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
