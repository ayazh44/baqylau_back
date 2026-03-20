from fastapi import APIRouter
from . import university_api

router = APIRouter(
    prefix="/university",
)

router.include_router(
    university_api.router,
    tags=["university"]

)