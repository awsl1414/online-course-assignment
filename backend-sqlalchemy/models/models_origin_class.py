from sqlalchemy import Column, Integer, String, Enum
from core import Base


class OriginClass(Base):
    __tablename__ = "OriginClassTable"
    id = Column(Integer, primary_key=True, index=True)
    teacherName = Column(String, nullable=False)
    teacherRoom = Column(String, nullable=False)
    courseName = Column(String, nullable=False)
    className = Column(String, nullable=False)
    population = Column(String, nullable=False)
    software = Column(String, nullable=False)
    cycle = Column(String, nullable=False)
