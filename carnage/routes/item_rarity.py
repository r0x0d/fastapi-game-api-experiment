from fastapi import APIRouter

from carnage.database.repository.item_rarity import ItemRarityRepository
from carnage.routes.schemas.item_rarity import (
    CreateItemRaritySchema,
    ListItemRaritySchema,
    UpdateItemRaritySchema,
)

router = APIRouter(prefix="/item_rarity", tags=["item-rarity"])
repository = ItemRarityRepository()


@router.get("/", response_model=list[ListItemRaritySchema])
async def get() -> list[ListItemRaritySchema]:
    result = repository.select()
    return [ListItemRaritySchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListItemRaritySchema)
async def get_by_id(identifier: str) -> ListItemRaritySchema:
    result = repository.select_by_id(identifier=identifier)
    return ListItemRaritySchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateItemRaritySchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateItemRaritySchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
