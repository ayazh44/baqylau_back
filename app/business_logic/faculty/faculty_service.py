from data_access.faculty.faculty_repository import FacultyRepository
from api.faculty.faculty_schemas import FacultyRead, FacultyCreate
from data_access.db.models.faculty import Faculty

class FacultyService:
    def __init__(self, repo: FacultyRepository):
        self.repo = repo

    async def get_all_faculties(self):
        return await self.repo.get_all()

    async def get_faculty_by_id(self, faculty_id: str):
        faculty = await self.repo.get_by_id(faculty_id)

        if not faculty:
            raise ValueError("Faculty not found")
        return faculty

    async def create(self, data: FacultyCreate):
        faculty = Faculty(
            title=data.title,
            dean=data.dean,
            university_id=data.university_id
        )

        return await self.repo.create(faculty)