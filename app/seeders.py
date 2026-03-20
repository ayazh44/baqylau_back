import asyncio
from sqlalchemy import select
from data_access.db.models.university import University
from data_access.db.models.faculty import Faculty
from data_access.db.session import AsyncSessionLocal


async def seed():
    async with AsyncSessionLocal() as db:
        universities = [
            {"name": "STU", "city": "Karaganda", "founded_year": 1953},
            {"name": "AIU", "city": "Astana", "founded_year": 2018}
        ]
        for u in universities:
            exists = (await db.execute(select(University).where(University.name == u["name"]))).scalar_one_or_none()
            if not exists:
                db.add(University(**u))
        await db.commit()

        stu = (await db.execute(select(University).where(University.name == "STU"))).scalar_one_or_none()
        aiu = (await db.execute(select(University).where(University.name == "AIU"))).scalar_one_or_none()
        if not stu or not aiu:
            raise Exception("Universities not found. Run universities seeder first.")

        faculties = [
            {"title": "Faculty of IT", "dean": "Ayazhan", "university_id": stu.id},
            {"title": "Faculty of Economics", "dean": "Molya", "university_id": aiu.id}
        ]
        for f in faculties:
            exists = (await db.execute(select(Faculty).where(Faculty.title == f["title"]))).scalar_one_or_none()
            if not exists:
                db.add(Faculty(**f))
        await db.commit()


if __name__ == "__main__":
    asyncio.run(seed())