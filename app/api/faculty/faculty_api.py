from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.faculty.faculty_schemas import FacultyCreate, FacultyRead
from business_logic.faculty.faculty_service import FacultyService
from data_access.faculty.faculty_repository import FacultyRepository

from data_access.db.session import get_db

router = APIRouter()

def get_facultys_service(db: AsyncSession = Depends(get_db)) -> FacultyService:
    repo = FacultyRepository(db)
    return FacultyService(repo)

@router.get("/", response_model=list[FacultyRead])
async def get_faculty(
    service: FacultyService = Depends(get_facultys_service),
):
    return await service.get_all_faculties()

@router.get("/{faculty_id}", response_model=FacultyRead)
async def get_faculty_by_id(faculty_id: str,
    service: FacultyService = Depends(get_facultys_service)):
    
    try:
        return await service.get_faculty_by_id(faculty_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/create", response_model=FacultyRead)
async def create(
    faculty: FacultyCreate,
    service: FacultyService = Depends(get_facultys_service),
):
    try:
        return await service.create(faculty)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))