from fastapi import APIRouter
from src.external.web.fastapi.api.endpoints import (
    availability,
)


router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello World"}

router.include_router(availability.router)

