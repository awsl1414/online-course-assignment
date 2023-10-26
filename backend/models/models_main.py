from sqlalchemy import Column, String, Integer, Enum
from core import Base


class ModelMain(Base):
    __tablename__ = "主表"
    id = Column(Integer, primary_key=True)
    teacherName = Column(String, nullable=False)

    courseName = Column(String, nullable=False)
    className = Column(String, nullable=False)
    classroomName = Column(String, nullable=False)
    week = Column(Integer, nullable=False)
    weekDay = Column(Integer, nullable=False)
    section = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    software = Column(String, nullable=False)
    measure = Column(Enum("0", "1", "2"), nullable=False)
