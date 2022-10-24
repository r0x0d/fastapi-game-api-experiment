from fastapi import APIRouter

from carnage.database.repository.account import AccountRepository
from carnage.routes.schemas.account import (
    CreateAccountSchema,
    ListAccountSchema,
    UpdateAccountSchema,
)

router = APIRouter(prefix="/account", tags=["account"])
repository = AccountRepository()


@router.get("/", response_model=list[ListAccountSchema])
async def get() -> list[ListAccountSchema]:
    result = repository.select()
    return [ListAccountSchema.from_orm(item) for item in result]


@router.get("/{identifier}", response_model=ListAccountSchema)
async def get_by_id(identifier: str) -> ListAccountSchema:
    result = repository.select_by_id(identifier=identifier)
    return ListAccountSchema.from_orm(result[0])


@router.post("/", status_code=201)
async def post(request: CreateAccountSchema) -> None:
    repository.insert(values=request.dict())


@router.put("/{identifier}", status_code=204)
async def put(
    request: UpdateAccountSchema,
    identifier: str,
) -> None:
    repository.update(values=request.dict(), identifier=identifier)


@router.delete("/{identifier}", status_code=204)
async def delete(identifier: str) -> None:
    repository.delete(identifier=identifier)
