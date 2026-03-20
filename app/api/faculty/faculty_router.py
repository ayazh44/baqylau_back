from fastapi import APIRouter
from . import faculty_api

router = APIRouter(
    prefix="/faculties",
)

router.include_router(
    faculty_api.router,
    tags=["faculties"]

)