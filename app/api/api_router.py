from api.faculty.faculty_router import router as faculty_router
from api.university.university_router import router as university_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(
    faculty_router,
    prefix="/api"  
)

api_router.include_router(
    university_router,
    prefix="/api"  
)