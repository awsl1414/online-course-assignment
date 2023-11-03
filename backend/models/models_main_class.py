from sqlalchemy import Column, String, Integer, Enum
from core import Base


class MainClass(Base):
    __tablename__ = "MainClassTable"
    id = Column(Integer, primary_key=True)
    teacherName = Column(String, nullable=False)
    courseName = Column(Enum("计算计网络", "无人机模拟"), nullable=False)
    population = Column(Integer, nullable=False)
    software = Column(String, nullable=False)
    classRoomName = Column(String, nullable=False)
    week = Column(Integer, nullable=False)
    weekDay = Column(Integer, nullable=False)
    lesson = Column(String, nullable=False)
    littleLesson = Column(String, nullable=False)
    cycle = Column(String, nullable=False)