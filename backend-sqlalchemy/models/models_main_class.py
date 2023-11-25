from sqlalchemy import Column, String, Integer, Enum
from core import Base


class MainClass(Base):
    __tablename__ = "MainClassTable"
    id = Column(Integer, primary_key=True, index=True)
    teacherName = Column(String, nullable=False)
    teacherRoom = Column(String, nullable=False)
    courseName = Column(String, nullable=False)
    className = Column(String, nullable=False)
    population = Column(String, nullable=False)
    software = Column(String, nullable=False)
    computerRoomName = Column(String, nullable=False)
    day = Column(String, nullable=False)
    lesson = Column(String, nullable=False)
    # 周期
    cycle = Column(String, nullable=False)
