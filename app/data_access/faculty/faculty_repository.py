from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models.faculty import Faculty
from api.faculty.faculty_schemas import FacultyRead, FacultyCreate


class FacultyRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[FacultyRead]:
        result = await self.db.execute(
            select(
                Faculty.id,
                Faculty.title,
                Faculty.dean,
                Faculty.university_id
            )
        )

        rows = result.all()

        return [
            FacultyRead(
                id=row.id,
                title=row.title,
                dean=row.dean,
                university_id=row.university_id
            )
            for row in rows
        ]

    async def get_by_id(self, faculty_id: str) -> FacultyRead | None:
        result = await self.db.execute(
            select(
                Faculty.id,
                Faculty.title,
                Faculty.dean,
                Faculty.university_id
            ).where(Faculty.id == faculty_id)
        )

        row = result.one_or_none()

        if row is None:
            return None

        return FacultyRead(
            id=row.id,
            title=row.title,
            dean=row.dean,
            university_id=row.university_id
        )

    async def create(self, faculty: FacultyCreate) -> FacultyRead:
        faculty = Faculty(
            title=faculty.title,
            dean=faculty.dean,
            university_id=faculty.university_id
        )

        self.db.add(faculty)
        await self.db.commit()
        await self.db.refresh(faculty)

        return FacultyRead(
            id=faculty.id,
            title=faculty.title,
            dean=faculty.dean,
            university_id=faculty.university_id
        )