from fastapi import APIRouter

from carnage.database.repository.item_base_type import ItemBaseTypeRepository
from carnage.routes.schemas.item_base_type import (
    CreateItemBaseTypeSchema,
    ListItemBaseTypeSchema,
    UpdateItemBaseTypeSchema,
)

router = APIRouter(prefix="/item_base_type", tags=["item-base-type"])
repository = ItemBaseTypeRepository()


@router.get("/", response_model=list[ListItemBaseTypeSchema])
async def get() -> list[ListItemBaseTypeSchema]:
    result = repository.select()
    return [ListItemBaseTypeSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListItemBaseTypeSchema)
async def get_by_id(identifier: str) -> ListItemBaseTypeSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListItemBaseTypeSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateItemBaseTypeSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateItemBaseTypeSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
