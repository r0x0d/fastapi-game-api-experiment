from fastapi import APIRouter

from carnage.database.repository.size import SizeRepository
from carnage.routes.schemas.size import (
    CreateSizeSchema,
    ListSizeSchema,
    UpdateSizeSchema,
)

router = APIRouter(prefix="/size", tags=["size"])
repository = SizeRepository()


@router.get("/", response_model=list[ListSizeSchema])
async def get() -> list[ListSizeSchema]:
    result = repository.select()
    return [ListSizeSchema.from_orm(item) for item in result]


@router.get("/<identifier>", response_model=ListSizeSchema)
async def get_by_id(identifier: str) -> ListSizeSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListSizeSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateSizeSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateSizeSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
