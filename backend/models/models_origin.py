from sqlalchemy import Column, Integer, String
from core import Base


class Origin(Base):
    __tablename__ = "原始表"
    id = Column(Integer, primary_key=True)
    teacherName = Column(String, nullable=False)
    courseName = Column(String, nullable=False)
    className = Column(String, nullable=False)
    classroomName = Column(String, nullable=False, comment="机房")
    population = Column(Integer, nullable=False)
    software = Column(String, nullable=False)
