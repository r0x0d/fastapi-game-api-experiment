from fastapi import APIRouter

from carnage.database.repository.item_magical_type import (
    ItemMagicalTypeRepository,
)
from carnage.routes.schemas.item_magical_type import (
    CreateItemMagicalTypeSchema,
    ListItemMagicalTypeSchema,
    UpdateItemMagicalTypeSchema,
)

router = APIRouter(prefix="/item_magical_type", tags=["item-magical-type"])
repository = ItemMagicalTypeRepository()


@router.get("/", response_model=list[ListItemMagicalTypeSchema])
async def get() -> list[ListItemMagicalTypeSchema]:
    result = repository.select()
    return [ListItemMagicalTypeSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListItemMagicalTypeSchema)
async def get_by_id(identifier: str) -> ListItemMagicalTypeSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListItemMagicalTypeSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateItemMagicalTypeSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateItemMagicalTypeSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
