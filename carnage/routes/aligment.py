from fastapi import APIRouter

from carnage.database.repository.aligment import AligmentRepository
from carnage.routes.schemas.aligment import (
    CreateAligmentSchema,
    ListAligmentSchema,
    UpdateAligmentSchema,
)

router = APIRouter(prefix="/aligment", tags=["aligment"])
repository = AligmentRepository()


@router.get("/", response_model=list[ListAligmentSchema])
async def get() -> list[ListAligmentSchema]:
    result = repository.select()
    return [ListAligmentSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListAligmentSchema)
async def get_by_id(identifier: str) -> ListAligmentSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListAligmentSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateAligmentSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateAligmentSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
