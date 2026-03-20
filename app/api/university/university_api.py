from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.university.university_schemas import UniversityCreate, UniversityRead
from business_logic.university.university_service import UniversityService
from data_access.university.university_repository import UniversityRepository
from data_access.db.session import get_db

router = APIRouter()


def get_university_service(
    db: AsyncSession = Depends(get_db),
) -> UniversityService:
    repo = UniversityRepository(db)
    return UniversityService(repo)


@router.get("/", response_model=list[UniversityRead])
async def get_universities(
    service: UniversityService = Depends(get_university_service),
):
    return await service.get_all()


@router.get("/{university_id}", response_model=UniversityRead)
async def get_university_by_id(
    university_id: str,
    service: UniversityService = Depends(get_university_service),
):
    university = await service.get_by_id(university_id)

    if not university:
        raise HTTPException(status_code=404, detail="University not found")

    return university


@router.post("/create", response_model=UniversityRead)
async def create_university(
    university: UniversityCreate,
    service: UniversityService = Depends(get_university_service),
):
    try:
        return await service.create(university)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))