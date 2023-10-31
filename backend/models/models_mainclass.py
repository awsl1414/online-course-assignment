from sqlalchemy import Column, String, Integer, Enum
from core import Base


class Main(Base):
    __tablename__ = "MainTable"
    id = Column(Integer, primary_key=True)
    teacherName = Column(String, nullable=False)
    courseName = Column(Enum("计算计网络", "无人机模拟"), nullable=False)
    population = Column(Integer, nullable=False)
    software = Column(String, nullable=False)
    classRoomName = Column(String, nullable=False)
    week = Column(Integer, nullable=False)
    weekDay = Column(Integer, nullable=False)
    className = Column(String, nullable=False)
    
    
    
    section = Column(Integer, nullable=False)
    
    
    measure = Column(Enum("0", "1", "2"), nullable=False, comment="小节")
