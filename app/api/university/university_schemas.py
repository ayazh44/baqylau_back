from pydantic import BaseModel
from typing import List
from uuid import UUID

class FacultyRead(BaseModel):
    id: UUID
    title: str
    dean: str

    class Config:
        orm_mode = True

class UniversityRead(BaseModel):
    id: UUID
    name: str
    city: str
    founded_year: int
    faculties: List[FacultyRead] = []

    class Config:
        orm_mode = True

class UniversityCreate(BaseModel):
    name: str
    city: str
    founded_year: int