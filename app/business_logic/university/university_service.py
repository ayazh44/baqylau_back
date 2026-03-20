from data_access.university.university_repository import UniversityRepository
from api.university.university_schemas import UniversityRead, UniversityCreate
from data_access.db.models.university import University

class UniversityService:
    def __init__(self, repo: UniversityRepository):
        self.repo = repo

    async def get_all(self):
        return await self.repo.get_all()

    async def get_by_id(self, university_id: str):
        university = await self.repo.get_by_id(university_id)

        if not university:
            raise ValueError("University not found")
        return university

    async def create(self, data: UniversityCreate):
        university = University(
            name=data.name,
            city=data.city,
            founded_year=data.founded_year
        )

        return await self.repo.create(university)