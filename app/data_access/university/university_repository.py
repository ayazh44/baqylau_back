from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from data_access.db.models.university import University
from api.university.university_schemas import UniversityRead, UniversityCreate


class UniversityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[UniversityRead]:
        result = await self.db.execute(
            select(
                University.id,
                University.name,
                University.city,
                University.founded_year
            )
        )
        rows = result.all()

        return [
            UniversityRead(
                id=row.id,
                name=row.name,
                city=row.city,
                founded_year=row.founded_year
            )
            for row in rows
        ]

    async def get_by_id(self, university_id: str) -> UniversityRead | None:
        result = await self.db.execute(
            select(
                University.id,
                University.name,
                University.city,
                University.founded_year
            ).where(University.id == university_id)
        )
        row = result.one_or_none()

        if row is None:
            return None

        return UniversityRead(
            id=row.id,
            name=row.name,
            city=row.city,
            founded_year=row.founded_year
        )

    async def create(self, university: UniversityCreate) -> UniversityRead:
        university = University(
            name=university.name,
            city=university.city,
            founded_year=university.founded_year
        )

        self.db.add(university)
        await self.db.commit()
        await self.db.refresh(university)

        return UniversityRead(
            id=university.id,
            name=university.name,
            city=university.city,
            founded_year=university.founded_year
        )