from sqlalchemy import (Column, String, Integer)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.sql import func
from data_access.db.base import Base

class University(Base):
    __tablename__ = "universities"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    founded_year = Column(Integer, nullable=False)

    faculties = relationship("Faculty", back_populates="university")
 