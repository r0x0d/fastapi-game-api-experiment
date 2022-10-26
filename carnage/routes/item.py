from fastapi import APIRouter

from carnage.database.repository.item import ItemRepository
from carnage.routes.schemas.item import (
    CreateItemSchema,
    ListItemSchema,
    UpdateItemSchema,
)

router = APIRouter(prefix="/item", tags=["item"])
repository = ItemRepository()


@router.get("/", response_model=list[ListItemSchema])
async def get() -> list[ListItemSchema]:
    result = repository.select()
    return [ListItemSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListItemSchema)
async def get_by_id(identifier: str) -> ListItemSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListItemSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateItemSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateItemSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
