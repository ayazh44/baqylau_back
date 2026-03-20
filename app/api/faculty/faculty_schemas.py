from pydantic import BaseModel
from uuid import UUID

class FacultyRead(BaseModel):
    id: UUID
    title: str
    dean: str
    university_id: UUID

    class Config:
        orm_mode = True

class FacultyCreate(BaseModel):
    title: str
    dean: str
    university_id: UUID